import sqlite3

conn = sqlite3.connect('data.db')
cur = conn.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        temp INTEGER NOT NULL,
        humidity TEXT NOT NULL
    )
''')

conn.commit()
conn.close()