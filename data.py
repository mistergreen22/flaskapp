import sqlite3

conn = sqlite3.connect('database.db')
print('Open database')

conn.execute('CREATE TABLE users (id INTEGER(20), name VARCHAR(20), surname VARCHAR(20), address VARCHAR(20))')
