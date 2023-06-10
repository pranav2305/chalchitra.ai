from dotenv import load_dotenv
import os
import openai
load_dotenv()

os.environ['OPENAI_API'] = os.getenv('OPEN_AI_API')

"""
# This function interacts with the GPT-3.5-turbo language model through the OpenAI API.

# It takes a user's query or message as input and returns the generated response.

 """
def convert_text_to_script(text, movie):

    prompt = f"""
    Generate a {movie} script for {text}
    Follow the JSON format given below strictly without spaces and new line or next line characters.
    Print the entire output in a single line. The output should have around 3500 characters
    JSON Format:
    {{
        title:"<movie_title">,
        speakers:[{{id:<speaker_id>,name:"<speaker_name">,gender:<"speaker_gender">}},]
        scenes:[{{description:"<scene_description>",
        dialogues:[{{speaker:"<speaker_id>",dialogue:"<dialogue_text>",expression:"<speaker_expression>"}},]}},]
    }}

    """

    openai.api_key = os.environ['OPENAI_API']

    # Call the OpenAI API to generate a response

    response = openai.ChatCompletion.create(

        model="gpt-3.5-turbo",

        messages=[{

            "role": "system",

            "content": "You are a fun yet knowledgable assistant."

        }, {

            "role": "user",

            "content": text

        }],

        temperature=0.6,

        max_tokens=150)

    print (response)

    # Return the generated speech and person information
    return (speech, person)