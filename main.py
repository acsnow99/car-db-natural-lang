
import os
import sys

from db import Database
from utils import *
from gpt import takingPrompt


def main(prompt_file):
    tempString = takingPrompt(compile_prompt(prompt_file_name = prompt_file))
    if (os.path.exists('taxi.db')):
        os.remove('taxi.db')
    database = Database('taxi.db')
    database.run_script('./sqlite/init.sql')

    query = takingPrompt(compile_prompt(prompt_file_name = prompt_file))
    print(compile_prompt(prompt_file_name = prompt_file))
    print(query)
    tempReponse = takingPrompt(compile_prompt('./prompts/init_response.txt', prompt_file) + "\nHere is the answer:" + str(database.execute(query)))
    with open('out.txt', 'a') as f:
       with open('./prompts/init.txt', 'r') as i:
        with open('./prompts/init_response.txt', 'r') as p:
            with open(prompt_file, 'r') as prompt:
                print("\n\nConversation", file=f)
                print(prompt.read(), file=f)
                print(query, file=f)
                print(compile_prompt('./prompts/init_response.txt', prompt_file), file=f)
                print(tempReponse, file=f)
            

            


def test():
    if (os.path.exists('taxi.db')):
        os.remove('taxi.db')
    database = Database('taxi.db')
    database.run_script('./sqlite/init.sql')

    print(database.execute('SELECT location FROM Landmark WHERE landmarkId = 3;'))


if (len(sys.argv)) > 1:
    main(sys.argv[1])
else:
    main('./prompts/simple.txt')
