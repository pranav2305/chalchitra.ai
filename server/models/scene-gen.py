import random

import torch
from stable_diffusion_videos import StableDiffusionWalkPipeline
from diffusers.utils.import_utils import is_xformers_available
from diffusers.models import AutoencoderKL
from diffusers.schedulers import LMSDiscreteScheduler


pipe = StableDiffusionWalkPipeline.from_pretrained(
    'runwayml/stable-diffusion-v1-5',
    torch_dtype=torch.float16,
    safety_checker=None,
    vae=AutoencoderKL.from_pretrained("stabilityai/sd-vae-ft-mse", torch_dtype=torch.float16).to("cuda"),
    scheduler=LMSDiscreteScheduler(
        beta_start=0.00085, beta_end=0.012, beta_schedule="scaled_linear"
    )
).to("cuda")

torch.cuda.empty_cache()
# Output video frames per second.
# Use lower values for testing (5 or 10), higher values for better quality (30 or 60)

# Convert seconds to frames
# This array should be `len(prompts) - 1` as its steps between prompts.

if is_xformers_available():
    pipe.enable_xformers_memory_efficient_attention()

# I give you permission to scrape this song :)
# youtube-dl -f bestaudio --extract-audio --audio-format mp3 --audio-quality 0 -o "music/thoughts.%(ext)s" https://soundcloud.com/nateraw/thoughts


# Output video frames per second.
# Use lower values for testing (5 or 10), higher values for better quality (30 or 60)
fps = 10

# Convert seconds to frames
# This array should be `len(prompts) - 1` as its steps between prompts.
# num_interpolation_steps = [(b-a) * fps for a, b in zip(audio_offsets, audio_offsets[1:])]
audio_offsets = [1,2,3]
num_interpolation_steps = [(b-a) * fps for a, b in zip(audio_offsets, audio_offsets[1:])]
# num_interpolation_steps = [20]

prompts = ["A forest from top, anime style", "A forest from top, anime style"]
seeds = [random.randint(0, 9e9) for _ in range(len(prompts))]

pipe.walk(
    prompts=prompts,
    seeds=seeds,
    num_interpolation_steps=num_interpolation_steps,
    fps=fps,
    output_dir = "output",
    # audio_filepath=audio_filepath,
    # audio_start_sec=audio_offsets[0],
    batch_size=2,  # Increase/decrease based on available GPU memory. This fits on 24GB A10
    num_inference_steps=2,
    guidance_scale=9,
    margin=1.0,
    smooth=0.2,
)