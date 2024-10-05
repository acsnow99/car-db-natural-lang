import requests
from db import Database
from utils import get_api_key

api_key = get_api_key('./config.json')
url = 'https://api.openai.com/v1/chat/completions'

auth = {
    'Authorization': f'Bearer {api_key}',
    'Accept': 'application/json'
}

database = Database('taxi.db')
    


def takingPrompt(prompt) -> str:
    response = requests.post(url, headers=auth, json={
    "model": "gpt-3.5-turbo",
    "messages": [
        {"role": "system", "content": "haha"},
        {"role": "user", "content": f"{prompt}"}
    ],
    "max_tokens": 100
    })

    if response.status_code == 200:
        temp = response.json()["choices"][0]["message"]["content"]
        try:
            return temp
        except Exception as error:
            print({error})
    else:
        return f"Failed {response.status_code}"