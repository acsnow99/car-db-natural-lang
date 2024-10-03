
import sqlite3

class Database:
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def execute(self, command):
        # Connect to SQLite (creates the DB file if it doesn't exist)
        connection = sqlite3.connect(self.connection_string)

        # Create a cursor object to execute SQL commands
        cursor = connection.cursor()

        # Create a new table
        cursor.execute(command)

        # Commit changes and close the connection
        return_value = connection.commit()
        connection.close()
        return return_value

database = Database('taxi.db')
database.execute('DROP TABLE car')
database.execute('CREATE TABLE car (VIN INT PRIMARY KEY, plate_number CHAR(6))')
database.execute('INSERT INTO car (VIN, plate_number) VALUES (123, "abcdef")')
print(database.execute('''SELECT car 
FROM sqlite_master 
WHERE type = 'table';'''))
