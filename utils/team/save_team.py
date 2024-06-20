from tkinter import messagebox
from persistence.team_dao import add_team_to_db, update_team_in_db
from persistence.config import TEAM_ATTRIBUTES

def save_team(entries, return_to_team_management_menu, team_id=None):
    team_data = {key: entry.get() for key, entry in entries.items()}
    missing_fields = [attr[0] for attr in TEAM_ATTRIBUTES if not team_data[attr[0]] and "NOT NULL" in attr[2]]
    
    if not missing_fields:
        if team_id is None:
            add_team_to_db(**team_data)
            messagebox.showinfo("Sucesso", "Time adicionado com sucesso!")
        else:
            update_team_in_db(team_id, **team_data)
            messagebox.showinfo("Sucesso", "Time atualizado com sucesso!")
        return_to_team_management_menu()
    else:
        messagebox.showerror(
            "Erro", 
            "Todos os campos mandatórios devem ser preenchidos. Tente novamente, por favor."
        )
