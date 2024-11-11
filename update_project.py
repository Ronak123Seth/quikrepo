import sqlite3

def view_and_update_project_status(contractor_id, project_id, new_status):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # Fetch projects assigned to this contractor
    cursor.execute('''
    SELECT * FROM forum WHERE assigned_to = ?
    ''', (contractor_id,))
    projects = cursor.fetchall()
    
    # Update project status
    cursor.execute('''
    UPDATE forum SET status = ? WHERE forum_id = ? AND assigned_to = ?
    ''', (new_status, project_id, contractor_id))
    
    conn.commit()
    conn.close()
    return projects
