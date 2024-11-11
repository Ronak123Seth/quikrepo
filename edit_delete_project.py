import sqlite3

def edit_project(project_id, new_title=None, new_description=None):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    if new_title:
        cursor.execute('''
        UPDATE forum SET title = ? WHERE forum_id = ?
        ''', (new_title, project_id))
    
    if new_description:
        cursor.execute('''
        UPDATE forum SET description = ? WHERE forum_id = ?
        ''', (new_description, project_id))
    
    conn.commit()
    conn.close()

def delete_project(project_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM forum WHERE forum_id = ?', (project_id,))
    
    conn.commit()
    conn.close()
