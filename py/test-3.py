import os
from openai import OpenAI

api_key = "AIzaSyC25qUk_nEVqkcqIGkkCrdki7yGM7G4AKk"
model = "gemini-1.5-flash"

BASE_URL = "https://llmapi.ultrasev.com/v2/gemini"

client = OpenAI(base_url=BASE_URL, api_key=api_key)
response = client.chat.completions.create(
    model=model,
    messages=[
        {"role": "system", "content": "You are a helpful assistant。"},
        {"role": "user", "content": "你好！你能帮我解决一下我的Python代码吗？"}
    ],
    temperature=0.7,
    top_p=1,
    max_tokens=1024,
    top_logprobs=32 # topK
)
print(response.choices[0].message.content)
