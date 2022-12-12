import json
import os
import openai

# Load your API key from an environment variable or secret management service
token = ""
with open("../conf.json") as f:
    data = json.load(f)
    # print("====== data:", type(data), data)
    token = data['token']
f.close()
# openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = token

response = openai.Image.create(
    prompt="a white siamese cat",
    n=1,
    size="1024x1024"
)
image_url = response['data'][0]['url']
print("image_url:", image_url)
