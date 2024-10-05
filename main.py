
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
    print(takingPrompt(compile_prompt('./prompts/init_response.txt', prompt_file) + "\nHere is the answer:" + str(database.execute(query))))
    with open('out.txt', 'w') as f:
        print('Filename:', 'output.txt', file=f)


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
