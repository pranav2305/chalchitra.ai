# chalchitra.ai
Transform your text into captivating, lipsynced animated videos effortlessly, with multilingual support including a wide range of Indian languages.

## Table of content
1. [Project Idea](#project-idea)
2. [Our Approach](our-approach)
3. [Challenges We Faced](#challenges-we-faced)
4. [Technologies We Used](#technologies-we-used)
5. [Network Diagram](#network-diagram)
6. [Installation and Setup Guide](#installation-and-setup-guide)
7. [Team Members](#team-members)

## Project Idea

## Our Approach

## Challenges We Faced

## Technologies We Used

## Network Diagram

## Installation and Setup Guide
To get started with Comicify.ai, follow these steps:
1. Clone the repo: <br>
`git clone https://github.com/pranav2305/chalchitra.ai.git`
2. Go to project directory <br>
`cd chalchitra.ai`

### Using the Next.js Frontend
1. Change directory to client <br>
`cd client`
2. Install npm packages <br>
`npm i`
3. Run the dev server <br>
`npm run dev`

### Using the Flask Backend
1. Change directory to server <br>
`cd server`
2. Create a .env file from .env.example
`cp .env.example .env`.
3. Update the API keys in .env: <br>
  a. `OPEN_AI_API = '<your-api-key>'`. Follow these instructions to obtain your key from OpenAI. <br>
  b. `STABLE_DIFFUSION_API = '<your-api-key>'`. Follow these instructions to obtain your key from Dream Studio. <br>
4. Create a virtual environment and activate it. <br>
`python -m venv env`
5. Install the requirements <br>
`python -r requirement.txt`
6. Get your Google Applications Credentials json file and activate it <br>
`export GOOGLE_APPLICATION_CREDENTIALS=<path_to_json_file>`
8. Run the flask server <br>
`flask --app main run`

### Using the SadTalker Model
Refer the [SadTalker README.md](https://github.com/pranav2305/chalchitra.ai/blob/main/server/models/SadTalker/README.md) for setup instructions

## Team Members

[Abhiraj Mengade](https://www.linkedin.com/in/abhiraj-mengade/)

[Parth Mittal](https://www.linkedin.com/in/mittal-parth)

[Pranav Agarwal](https://www.linkedin.com/in/ag-pranav)
