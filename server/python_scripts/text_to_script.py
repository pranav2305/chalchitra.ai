from dotenv import load_dotenv
import os
import openai
import json

load_dotenv()

os.environ['OPENAI_API'] = os.getenv('OPEN_AI_API')

"""
# This function interacts with the GPT-3.5-turbo language model through the OpenAI API.

# It takes a user's query or message as input and returns the generated response.

 """
def generate_script_from_text(text):

    prompt = f"""
        Create a meaningful story about {text} with the following constraints.
        The entire story should have 1-2 scenes and a minimum of 2 dialogues.
        Follow the JSON format given below strictly without spaces and new line or next line characters.
        Print the entire output in a single line. Make sure to complete the json.
        JSON Format:
        {{"title":"<movie_title>","speakers<list_of_all_speakers>":[{{"id":<speaker_id>,"name":"<speaker_name">,"gender":"<speaker_gender>","visual":"<visual_desc_of_speaker>"}}]"scenes":[{{"description":"<scene_description>","narrator":"<narrator_dialogue>","dialogues":[{{"speaker":"<speaker_id>","dialogue":"<dialogue_text>","expression":"<speaker_expression>"}}]}}]}}
    """

    print(prompt)

    # Sample response from the API
    # res_json = """
    #     {"title":"The Brave Heart","speakers":[{"id":1,"name":"Priya","gender":"female","visual":"An Indian girl with short hair and determined eyes"}],"scenes":[{"description":"Priya at the Army Recruitment Office","narrator":"Priya walked into the Army Recruitment Office with her head held high.","dialogues":[{"speaker":1,"dialogue":"I want to join the Indian Army.","expression":"determined"}]}]}
    # """

    # return json.loads(res_json)

    openai.api_key = os.environ['OPENAI_API']

    # Call the OpenAI API to generate a response

    response = openai.ChatCompletion.create(

        model="gpt-3.5-turbo",

        messages = [
            {'role': 'user', 'content': prompt}
        ],

        temperature=0.6,

        max_tokens=500)

    print(response)

    res_json = response["choices"][0]["message"]["content"]
    # remove whitespaces, / and /n from the response
    # res_json = res_json.replace(" ", "")
    res_json = res_json.replace("\n", "")
    res_json = res_json.replace("\\", "")

    print(res_json)

    data = json.loads(res_json)

    # Return the generated speech and person information
    return data