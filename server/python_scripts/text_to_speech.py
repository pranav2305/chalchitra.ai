"""Synthesizes speech from the input string of text or ssml.
Make sure to be working in a virtual environment.

Note: ssml must be well-formed according to:
    https://www.w3.org/TR/speech-synthesis/

Remember to set GOOGLE_APPLICATION_CREDENTIALS=<PATH> for deployment
"""
from google.cloud import texttospeech
import os

def generate_speech_from_text(target, text, gender, i):
    result_dir = "./results/audios"

    # Instantiates a client
    client = texttospeech.TextToSpeechClient()

    # Set the text input to be synthesized
    synthesis_input = texttospeech.SynthesisInput(text=text)

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    # Map the 'gender' variable to the corresponding SSML voice gender
    ssml_gender = texttospeech.SsmlVoiceGender.MALE if gender == 'male' else texttospeech.SsmlVoiceGender.FEMALE
    name_type = 'B' if gender == 'male' else 'A'
    name = target + '-Wavenet-' + name_type

    voice = texttospeech.VoiceSelectionParams(
        language_code=target,
        ssml_gender=ssml_gender,
        name=name
    )

    # Select the type of audio file you want returned
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # The response's audio_content is binary.
    filepath = os.path.join(result_dir, str(i) + '.mp3')
    with open(filepath, "wb") as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        print('Audio content written to file {}'.format(filepath))

    return filepath