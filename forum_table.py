import sqlite3

# Connect to SQLite database (create if it doesn't exist)
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Create the forum table
cursor.execute('''
CREATE TABLE IF NOT EXISTS forum (
    forum_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    dept_id INTEGER,
    title TEXT,
    description TEXT,
    status TEXT DEFAULT 'Pending',
    date_time TEXT,
    created_by TEXT,
    assigned_to TEXT
);
''')

conn.commit()
conn.close()
