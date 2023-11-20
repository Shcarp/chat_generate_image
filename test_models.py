import os
from dotenv import load_dotenv
from chat import ChatGPT

load_dotenv()

API_KEY = os.getenv('OPENAI_API_KEY')

_MODELS_MAP = [
    {
        'name': 'DreamShaper XL1.0',
        'description': 'realistic images, graphics, and faces.',
        'unfit': f"This model is very unfriendly to Asians, especially Chinese, Japanese and Korean women, with single eyelids, zombie faces, and I don't know where the 'traditional' clothes come from, even if I add double eyelids and bikinis as cues, it still doesn't change the stereotypical image.",
    },
    {
        'name': 'Anything V5',
        'description': 'anime, 2D',
        'unfit': "actual 3D is so bad"
    }
]

def get_model_info(name, description, unfit):
    template = f"{name} is a model, It can generate {description} images, that defect is {unfit}"
    return template

model_info = []

for model in _MODELS_MAP:
    model_info.append(get_model_info(model['name'], model['description'], model['unfit']))

system_prompt = "Help me choose a model for my prompt. You just need to return the model name. model Info: " + ", ".join(model_info)

client = ChatGPT(
    key=API_KEY, 
    model="gpt-4",
    system_prompt=system_prompt,    
)

client.ask("A beautiful woman, dirty blonde hair with brown highlights, shoulder length hair, brown eyes, slightly wavy hair, Caucasian, in Greek armor, teenage girl, cartoon style, soft jawline, cartoon style")
