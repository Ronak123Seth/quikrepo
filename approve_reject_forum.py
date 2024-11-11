import sqlite3
from datetime import datetime

def approve_or_reject_forum(admin_id, forum_id, action, date_time=None):
    conn = sqlite3.connect('project_database.db')
    cursor = conn.cursor()
    
    if action == 'accept':
        date_time = date_time or datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute('''
        UPDATE forum SET status = 'Approved', date_time = ? WHERE forum_id = ?
        ''', (date_time, forum_id))
    elif action == 'reject':
        cursor.execute('''
        UPDATE forum SET status = 'Rejected' WHERE forum_id = ?
        ''', (forum_id,))
    
    conn.commit()
    conn.close()
