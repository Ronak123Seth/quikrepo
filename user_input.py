import sqlite3

def insert_forum(user_id, dept_id, title, description, created_by, assigned_to):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    INSERT INTO forum (user_id, dept_id, title, description, created_by, assigned_to) 
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (user_id, dept_id, title, description, created_by, assigned_to))
    
    conn.commit()
    conn.close()
