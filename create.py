import sqlite3

# create a connection
connection = sqlite3.connect('sample.db')

# create a table
table = 'CREATE TABLE People (id integer primary key, name TEXT, surname TEXT)'

# create a curseor to interact with the db
cursor = connection.cursor()
cursor.execute(table)

# finally commit changes
connection.commit()