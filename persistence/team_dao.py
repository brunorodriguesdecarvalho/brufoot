import json
from .database import create_connection
from .config import TEAM_ATTRIBUTES, get_column_names

def execute_query(query, params=(), fetch=False):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(query, params)
    if fetch:
        results = cursor.fetchall()
        conn.close()
        return results
    conn.commit()
    conn.close()

def add_team_to_db(**kwargs):
    columns = ", ".join(kwargs.keys())
    placeholders = ", ".join(["?" for _ in kwargs])
    query = f'INSERT INTO teams ({columns}) VALUES ({placeholders})'
    params = tuple(json.dumps(kwargs[key]) if key == "players" else kwargs[key] for key in kwargs)
    execute_query(query, params)

def get_teams_from_db():
    columns = ", ".join(["id"] + get_column_names(TEAM_ATTRIBUTES))
    query = f"SELECT {columns} FROM teams"
    teams = execute_query(query, fetch=True)
    return [
        {attr: (json.loads(row[idx]) if attr == "players" else row[idx])
         for idx, attr in enumerate(["id"] + get_column_names(TEAM_ATTRIBUTES))}
        for row in teams
    ]

def delete_team_from_db(team_id):
    query = "DELETE FROM teams WHERE id = ?"
    params = (team_id,)
    execute_query(query, params)

def update_team_in_db(team_id, **kwargs):
    set_clause = ", ".join([f"{key} = ?" for key in kwargs])
    query = f'UPDATE teams SET {set_clause} WHERE id = ?'
    params = tuple(json.dumps(kwargs[key]) if key == "players" else kwargs[key] for key in kwargs) + (team_id,)
    execute_query(query, params)
