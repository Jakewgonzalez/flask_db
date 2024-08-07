import sqlite3
from werkzeug.security import generate_password_hash

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

cur.execute('''
    CREATE TABLE IF NOT EXISTS profile (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        last_login TIMESTAMP
    )
''')

conn.commit()
conn.close()

def user_add(username, password):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()

    password_hash = generate_password_hash(password)

    cur.execute('''
        INSERT INTO profile (username, password_hash)
        VALUES (?, ?)
    ''', (username, password_hash))
    
    conn.commit()
    conn.close()

#user_add('admin', 'root')
#user_add('user', 'pass')