import os
import requests
api_key = os.getenv('')
url = 'https://api.openai.com/v1/chat/completions'

headers = {
    'Authorization': f'Bearer {api_key}',
    'Accept': 'application/json'
}

data = {
    "model": "gpt-4",
    "messages": [ 
        {"role": "system", "content": "haha"},
        {"role": "user", "content": "Write a sql query"}
    ],
    "max_tokens": 100
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    result = response.json()
    print(result)
else:
    print(f"Failed")