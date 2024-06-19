TEAM_ATTRIBUTES = [
    ("name", "TEXT", "NOT NULL", "* Nome"),
    ("country", "TEXT", "NOT NULL", "* País"),
    ("state", "TEXT", "", "Estado"),
    ("city", "TEXT", "", "Cidade"),
    ("initial_level", "INTEGER", "NOT NULL CHECK(initial_level >= 0 AND initial_level <= 100)", "* Nível Inicial"),
    ("stadium_id", "INTEGER", "", "ID do Estádio"),
    ("primary_color", "TEXT", "NOT NULL", "* Cor Principal"),
    ("secondary_color", "TEXT", "NOT NULL", "* Cor Secundária"),
    ("coach_id", "INTEGER", "", "ID do Treinador"),
]

def get_column_names(attributes):
    return [attr[0] for attr in attributes]
