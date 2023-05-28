import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name TEXT, price REAL)"
cursor.execute(create_table)

cursor.execute("INSERT INTO items VALUES(NULL, ?, ?)", ('Sofa', 44.99))

connection.commit()

connection.close()
