import tkinter as tk

def edit_team(tree, team_ids, switch_frame_to_edit_team):
    selected_item = tree.selection()
    if selected_item:
        item = tree.item(selected_item)
        team_data = item['values']
        team_id = team_ids[tree.index(selected_item[0])]
        switch_frame_to_edit_team(team_data, team_id)
    else:
        tk.messagebox.showerror("Erro", "Nenhum time selecionado.")
