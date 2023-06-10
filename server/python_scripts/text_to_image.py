# Create an image from the generated speech and person information using the Stable Diffusion API
from dotenv import load_dotenv
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation
from PIL import Image
import os
import warnings
import io

load_dotenv()

os.environ['STABILITY_HOST'] = os.getenv('STABILITY_HOST')
os.environ['STABILITY_KEY'] = os.getenv('STABLE_DIFFUSION_API')

stability_api = client.StabilityInference(
    key=os.environ['STABILITY_KEY'],
    verbose=True,
    engine="stable-diffusion-xl-beta-v2-2-2",
)

def generate_image_from_text(character, action_or_place, feeling, gender, i):

    answer = stability_api.generate(
        prompt=f"""
        Create a comic-style image where {character} is {action_or_place}
        with the an {feeling} expression. Gender - {gender}
        """,

        seed=992446758,

        width=512,

        height=512,

        samples=1,

        sampler=generation.SAMPLER_K_DPMPP_2M

    )

    # Check if the folder exists, create it if necessary

    folder_path = "./images"
    # Save the generated image to the folder

    print(answer)

    for resp in answer:

        for artifact in resp.artifacts:

            if artifact.finish_reason == generation.FILTER:

                warnings.warn(

                    "Your request activated the API's safety filters and could not be processed."

                    "Please modify the prompt and try again.")

            if artifact.type == generation.ARTIFACT_IMAGE:

                image_path = os.path.join(folder_path, f"{i}.png")
                print(image_path)

                img_binary = io.BytesIO(artifact.binary)

                img = Image.open(img_binary)

                img.save(image_path)

                return image_path
