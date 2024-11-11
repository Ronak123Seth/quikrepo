import sqlite3

def view_projects_by_creator(dept_rep_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    SELECT * FROM forum WHERE created_by = ?
    ''', (dept_rep_id,))
    
    projects = cursor.fetchall()
    conn.close()
    return projects
