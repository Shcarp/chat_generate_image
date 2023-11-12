import os
import requests
from chat import ChatGPT
from image import Image
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')


def optimization_prompt(easy_prompt):
    print("call optimization_prompt: " + easy_prompt)
    optimizate = ChatGPT(
        key=API_KEY, 
        model="ft:gpt-3.5-turbo-1106:onbrand-inc::8Jyggva9",
        system_prompt="You are autoregressive language model that works at openart.ai and specializes in creating perfect, outstanding prompts for generative art models like Stable Diffusion. Your job is to take user ideas, capture ALL main parts, and turn into amazing prompts. You have to capture everything from the user's prompt and then use your talent to make it amazing. You are a master of art styles, terminology, pop culture, and photography across the globe. Respond only with the new prompt.",    
    )
    back_content = optimizate.ask(easy_prompt).content
    print("back_content: " + back_content)
    return back_content

def generate_image(prompt):
    print("call generate_image: " + prompt)
    print("generate_image: " + prompt)
    client = Image(
        key=API_KEY,
        model="dall-e-3",
    )

    url = client.generate_image(
        prompt=prompt
    )

    print("generate_image: " + url)
    return "Generate image: " + url

def image2image(image_url, prompt):
    print("call image2image: " + prompt)
    print("image2image: " + image_url)
    client = Image(
        key=API_KEY,
        model="dall-e-3",
    )

    # 通过url获取图片
    image = requests.get(image_url).content

    url = client.edit_image(
        prompt=prompt,
        image=image,
        mask=None,
    )
    
    print("image2image: " + url)

    return "Generate image: " + url


def main():
    chat = ChatGPT(
        key=API_KEY, 
        model="gpt-4",
        system_prompt=""
    )

    chat.add_tool(
        func=optimization_prompt, 
        description="This function optimizes a simple prompt to help with image generation",
        schema={"type": "object", "properties": {"easy_prompt": {"type": "string", "description": "simple prompt"}}, "required": ["easy_prompt"]},
    )

    chat.add_tool(
        func=generate_image,
        description="This function generates an image using a prompt",
        schema={"type": "object", "properties": {"prompt": {"type": "string", "description": "prompt"}}, "required": ["prompt"]},
    )

    chat.add_tool(
        func=image2image,
        # 这个tool 可以用来修改之前生成的图片, 使用prompt来修改, 需要传入之前生成的图片的url
        description="This function modifies an image using a prompt and old image",
        schema={
            "type": "object", 
            "properties": {
                "image_url": {
                    "type": "string", 
                    "description": "image url"
                }, 
                "prompt": {
                    "type": "string", 
                    "description": "prompt"
                }
            }, 
                "required": ["image_url", "prompt"]
        },
    )

    while True:
        question = input("You: ")
       
        print("Me: " + question)

        response = chat.ask(question)

        print("Bot: " + response.content)


if __name__ == "__main__":
    main()
