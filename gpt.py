import os
import requests
from db import Database

api_key = ''
url = 'https://api.openai.com/v1/chat/completions'

auth = {
    'Authorization': f'Bearer {api_key}',
    'Accept': 'application/json'
}

database = Database('taxi.db')

def takingPrompt(prompt):
    response = requests.post(url, headers=auth, json={
    "model": "gpt-4",
    "messages": [ 
        {"role": "system", "content": "haha"},
        {"role": "user", "content": f"{prompt}"}
    ],
    "max_tokens": 100
    })
    if response.status_code == 200:
        print(f"Failed {response}")
        temp = response.json()["choices"][0]["message"]["content"]
        try:
            result = database.execute(temp)
            print("Query Result:")
            print(result)
        except Exception as error:
            print({error})
    else:
        print(f"Failed {response.status_code}")
