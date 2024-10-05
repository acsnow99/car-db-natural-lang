
import sqlite3
import os

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


if (os.path.exists('taxi.db')):
    os.remove('taxi.db')
database = Database('taxi.db')
database.run_script('./sqlite/init.sql')

print(database.execute('SELECT * FROM RideRecord;'))

