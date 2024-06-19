import sqlite3
from .config import TEAM_ATTRIBUTES

def create_connection():
    return sqlite3.connect('brufoot.db')

def create_tables():
    conn = create_connection()
    cursor = conn.cursor()
    columns = ", ".join([f"{attr[0]} {attr[1]} {attr[2]}" for attr in TEAM_ATTRIBUTES])
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS teams (
            id INTEGER PRIMARY KEY,
            {columns}
        )
    ''')
    conn.commit()
    conn.close()
