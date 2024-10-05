import os
import requests
from main import Database

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
database = Database('taxi.db')
def pushToDatabase():
    if response.status_code == 200:
        temp = response.json()
        try:
            result = database.execute(temp)
            print("Query Result:")
            print(result)
        except Exception as error:
            print({error})
    else:
        print(f"Failed")

def takingPrompt(prompt):
    response = requests.post(url, headers=auth, json={
    "model": "gpt-4",
    "messages": [ 
        {"role": "system", "content": "haha"},
        {"role": "user", "content": {prompt}}
    ],
    "max_tokens": 100
    })
    if response.status_code == 200:
        temp = response.json()
        try:
            result = database.execute(temp)
            print("Query Result:")
            print(result)
        except Exception as error:
            print({error})
    else:
        print(f"Failed")
