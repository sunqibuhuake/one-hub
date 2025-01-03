import subprocess
import json

api_key = "sk-kQKMTKyEQA7X6eZ_8eKZ6PRLhSU-aC2L-jcozusWiMRPpZRMbhd2sOVuSeo"
endpoint = "http://localhost:3030/v1/chat/completions"

# Define the data you want to send
data = {
    "model": "gemini-1.5-pro",  # You can use gpt-4-turbo or other models
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello! Can you help me with my Python code?"}
    ]
}

# Convert the data to JSON format
data_json = json.dumps(data)

# Call the OpenAI API via curl using subprocess
response = subprocess.run(
    [
        "curl",
        "-X", "POST",
        endpoint,
        "-H", f"Content-Type: application/json",
        "-H", f"Authorization: Bearer {api_key}",
        "-d", data_json
    ],
    capture_output=True,
    text=True
)

# Print the response
print(response.stdout)
