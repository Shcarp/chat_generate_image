from openai import OpenAI

class Image:
    def __init__(self, key, model):
        self.key = key
        self.gpt = OpenAI(api_key=key)
        self.model = model
        self.client = self.gpt.images

    def generate_image(self, prompt):
        response = self.client.generate(
            model=self.model,
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )

        image_url = response.data[0].url

        return image_url
    
    def edit_image(self, prompt, image, mask):
        response = self.client.edit(
            model=self.model,
            image=image,
            mask=mask,
            prompt=prompt
        )

        image_url = response.data[0].url

        return image_url

