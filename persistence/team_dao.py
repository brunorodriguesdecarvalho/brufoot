from .database import create_connection

def insert_team(name, city, stadium, skill_level):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO teams (name, city, stadium, skill_level)
        VALUES (?, ?, ?, ?)
    ''', (name, city, stadium, skill_level))
    conn.commit()
    conn.close()

def get_all_teams():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM teams')
    teams = cursor.fetchall()
    conn.close()
    return teams
