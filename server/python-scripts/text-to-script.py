from dotenv import load_dotenv
import os
import openai
load_dotenv()

os.environ['OPENAI_API'] = os.getenv('OPEN_AI_API')

"""
# This function interacts with the GPT-3.5-turbo language model through the OpenAI API.

# It takes a user's query or message as input and returns the generated response.

 """
def convert_text_to_script(text):

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

    # Process the response to extract speech and person information

    speech, person = generate_map_from_text(
        response.choices[0].message.content)

    # Return the generated speech and person information
    return (speech, person)