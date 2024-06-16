import sqlite3

def create_tables():
    conn = sqlite3.connect('brufoot.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS teams (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        city TEXT NOT NULL,
        stadium TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

def add_team_to_db(name, city, stadium):
    conn = sqlite3.connect('brufoot.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO teams (name, city, stadium) VALUES (?, ?, ?)', (name, city, stadium))
    conn.commit()
    conn.close()

def get_teams_from_db():
    conn = sqlite3.connect('brufoot.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, city, stadium FROM teams")
    teams = cursor.fetchall()
    conn.close()
    return [{"id": row[0], "name": row[1], "city": row[2], "stadium": row[3]} for row in teams]

def delete_team_from_db(team_id):
    conn = sqlite3.connect('brufoot.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM teams WHERE id = ?", (team_id,))
    conn.commit()
    conn.close()

def update_team_in_db(team_id, new_name, new_city, new_stadium):
    conn = sqlite3.connect('brufoot.db')
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE teams 
        SET name = ?, city = ?, stadium = ? 
        WHERE id = ?
    """, (new_name, new_city, new_stadium, team_id))
    conn.commit()
    conn.close()