import json
from flask import request

input_url = input("Enter your long URL: ")

headers = {
    "accept": "application/json",
}

params = {
    "api_token": "FNkHWzua9nlntBnIFK2gvI6hKl8dy0yPOpNoVaXPpummcai3sAkkW3Z7nJuk",
}

json_data = {
    "url": input_url,
    "domain": "tiny.one",
    "alias": "stuycslink",
    "tags": "cs",
    "expires_at": "2024-11-28 12:00:00",
}

response = request.post('https://api.tinyurl.com/create', params=params, headers=headers, json=json_data)

# parsing
response = (response.text)
json_load = json.loads(response)
tinyurl=(json_load['data']['tiny_url'])
longurl=(json_load['data']['url'])
print(f"Here's your long URL: {{longurl}}")
print(f"Here's your shortened URL: {{tinyurl}}")
