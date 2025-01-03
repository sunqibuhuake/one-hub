import subprocess
import json

api_key = "sk-kQKMTKyEQA7X6eZ_8eKZ6PRLhSU-aC2L-jcozusWiMRPpZRMbhd2sOVuSeo"
# endpoint = "http://localhost:3000/v1/chat/completions"

# Define the data you want to send
# data = {
#     "model": "gemini-1.5-pro",  # You can use gpt-4-turbo or other models
#     "messages": [
#         {"role": "system", "content": "You are a helpful assistant."},
#         {"role": "user", "content": "Hello! Can you help me with my Python code?"}
#     ]
# }

# Convert the data to JSON format
# data_json = json.dumps(data)

# Call the OpenAI API via curl using subprocess
response = subprocess.run(
    [
        "curl",
        "-X", "POST",
        "http://localhost:3001/api/proxy/v1beta/models/gemini-1.5-flash:generateContent?key=AIzaSyC25qUk_nEVqkcqIGkkCrdki7yGM7G4AKk",
        "-H", f"Content-Type: application/json",
        "--data-raw", '{"contents":[{"role":"user","parts":[{"text":"Hello Gemini"}]}]}',
        "--compressed"
    ],
    capture_output=True,
    text=True
)

# Print the response
print(response.stdout)
