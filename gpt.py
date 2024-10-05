import os
import requests
api_key = os.getenv('')
url = 'https://api.openai.com/v1/chat/completions'

auth = {
    'Authorization': f'Bearer {api_key}',
    'Accept': 'application/json'
}

content = {
    "model": "gpt-4",
    "messages": [ 
        {"role": "system", "content": "haha"},
        {"role": "user", "content": "Write a sql query"}
    ],
    "max_tokens": 100
}

response = requests.post(url, headers=auth, json=content)

if response.status_code == 200:
    temp = response.json()
    print(temp)
else:
    print(f"Failed")