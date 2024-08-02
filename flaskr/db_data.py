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

cur.executemany('''
    INSERT INTO users (name, temp, humidity)
    VALUES (?, ?, ?)
''', [
    ('Sensor 1', 30, 14),
    ('Sensor 2', 25, 11)
])

conn.commit()
conn.close()