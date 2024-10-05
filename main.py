
import sqlite3
import os
import sys
from gpt import takingPrompt

def main(prompt_file):
    if (os.path.exists('taxi.db')):
        os.remove('taxi.db')
    database = Database('taxi.db')
    database.run_script('./sqlite/init.sql')
    takingPrompt(compile_prompt(prompt_file))

def test():
    if (os.path.exists('taxi.db')):
        os.remove('taxi.db')
    database = Database('taxi.db')
    database.run_script('./sqlite/init.sql')

    print(database.execute('SELECT location FROM Landmark WHERE landmarkId = 3;'))




class Database:
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def execute(self, command, is_script = False):
        # Connect to SQLite (creates the DB file if it doesn't exist)
        connection = sqlite3.connect(self.connection_string)

        # Create a cursor object to execute SQL commands
        cursor = connection.cursor()

        # Create a new table
        if (is_script):
            cursor.executescript(command)
        else:
            cursor.execute(command)

        return_value = cursor.fetchall()

        # Commit changes and close the connection
        connection.commit()
        connection.close()
        return return_value
    
    def run_script(self, file_name):
        with open(file_name, 'r') as file:
            init_command = file.read()

        return self.execute(init_command, True)


def compile_prompt(prompt_file_name = './prompts/simple.txt'):
    with open('./prompts/init.txt') as init_file:
        init_prompt = init_file.read()
    with open(prompt_file_name) as prompt_file:
        core_prompt = prompt_file.read()

    return init_prompt + '\n' + core_prompt




if (len(sys.argv)) > 1:
    main(sys.argv[1])
else:
    main(prompt_file='./prompts/simple.txt')
