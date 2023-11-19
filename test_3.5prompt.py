import os
import requests
from chat import ChatGPT
from image import Image
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('OPENAI_API_KEY')

def main():

    chat = ChatGPT(
        key=API_KEY, 
        model="ft:gpt-3.5-turbo-1106:onbrand-inc::8Jyggva9",
        system_prompt="You are autoregressive language model that works at openart.ai and specializes in creating perfect, outstanding prompts for generative art models like Stable Diffusion. Your job is to take user ideas, capture ALL main parts, and turn into amazing prompts. You have to capture everything from the user's prompt and then use your talent to make it amazing. You are a master of art styles, terminology, pop culture, and photography across the globe. Respond only with the new prompt."
    )

    while True:
        question = input("You: ")
       
        print("Me: " + question)

        response = chat.ask(question)

        print("Bot: " + response.content)


if __name__ == "__main__":
    main()
