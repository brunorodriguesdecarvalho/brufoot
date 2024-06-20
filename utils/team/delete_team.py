from tkinter import messagebox
from persistence.team_dao import delete_team_from_db

def delete_team(tree, team_ids, update_teams_list):
    selected_item = tree.selection()
    if selected_item:
        index = tree.index(selected_item)
        team_id = team_ids[index]  # Busca o ID correspondente pelo índice
        delete_team_from_db(team_id)
        update_teams_list()
    else:
        messagebox.showerror("Erro", "Nenhum time selecionado.")
