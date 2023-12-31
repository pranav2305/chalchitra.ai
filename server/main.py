from flask import Flask, request, jsonify, send_file
# from flask_cors import CORS
from python_scripts.text_to_script import generate_script_from_text
from python_scripts.text_to_image import generate_image_from_text
from python_scripts.translate import translate_text
from python_scripts.text_to_speech import generate_speech_from_text
from python_scripts.generate_lip_sync import generate_lip_sync
# from python_scripts.stitch_videos import stitch_videos
from python_scripts.stitch import stitch_videos
from datetime import datetime

app = Flask(__name__)

# CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/', methods=['GET'])
def test():
    """
    Endpoint to check if the server is running.

    Returns:
        str: A string indicating that the server is running.

    Methods:
        GET

    Returns:
        str: A string indicating that the server is running.
    """
    return 'The server is running!'

@app.route('/', methods=['POST'])
def generate_movie_from_text():

    user_input = request.get_json()['userInput']
    language = request.get_json()['language']
    # language = 'hi-IN'
    language_code = language.split('-')[0]
    response = generate_script_from_text(user_input)
    # response = generate_script_from_text("An indian girl trying to enter the army")

    print(response)
    # use timestamp as story_id
    story_id = datetime.now().strftime("%Y%m%d%H%M%S")

    generated_videos_paths = []
    subtitles = []

    scenes = response['scenes']
    speakers = response['speakers']
    no_of_scenes = len(scenes)

    for i in range(no_of_scenes):
        scene = scenes[i]
        dialogues = scene['dialogues']
        narrator = scene['narrator']

        for j, dialogue in enumerate(dialogues):
            speaker_id = dialogue['speaker']
            speaker = next((sp for sp in speakers if sp['id'] == speaker_id), None)

            if speaker:
                character = speaker['name']
                action_or_place = narrator
                feeling = dialogue['expression']
                gender = speaker['gender']

                # Call the generate_image_from_text function with the appropriate parameters
                image_path = generate_image_from_text(character, action_or_place, feeling, gender, f"{story_id}_{i}_{j}")
                print(image_path)

                subtitles.append(dialogue['dialogue'])
                translated_text = translate_text(language_code, dialogue['dialogue'])
                print(translated_text)

                # Call the generate_speech_from_text function with the appropriate parameters
                speech_path = generate_speech_from_text(language, translated_text, gender, f"{story_id}_{i}_{j}")

                # Call the generate_lip_sync function with the appropriate parameters
                lip_sync_path = generate_lip_sync(image_path, speech_path, f"{story_id}_{i}_{j}")
                print(lip_sync_path)

                generated_videos_paths.append(lip_sync_path)

            else:
                print(f"Speaker with id {speaker_id} not found.")

    # Call stitch videos
    stitch_videos(generated_videos_paths, f"./results/outputs/{story_id}_output.mp4")
    return send_file(f"./results/outputs/{story_id}_output.mp4", mimetype='video/mp4', as_attachment=True)
