import os
import requests
from chat import ChatGPT
from image import Image
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')

# 我需要你从这个网站上获取一些基数的数据，然后我问你一些问题，你需要根据这些数据来回答我的问题
# english: I need you to get some data from this website, then i ask you some questions, you need to answer my questions based on this data. this is my website: https://stable-diffusion-art.com/prompt-guide/#Anatomy_of_a_good_prompt

def main():


    chat = ChatGPT(
        key=API_KEY, 
        model="gpt-4",
        system_prompt="I need you to get some data from this website, then i ask you some questions, you need to answer my questions based on this data. this is my website: https://stable-diffusion-art.com/prompt-guide/#Anatomy_of_a_good_prompt"
    )

    while True:
        question = input("You: ")
       
        print("Me: " + question)

        response = chat.ask(question)

        print("Bot: " + response.content)


if __name__ == "__main__":
    main()
