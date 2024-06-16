import tkinter as tk
from tkinter import messagebox
from persistence.database import update_team_in_db
from ui.frames.base_frame import BaseFrame

class TeamEditFrame(BaseFrame):
    def __init__(self, master, switch_frame, team_data):
        super().__init__(master, switch_frame)
        self.switch_frame = switch_frame
        self.team_data = team_data
        self.create_widgets()

    def create_widgets(self):

        #Título 
        title_label = tk.Label(self.frame, text="BruFoot", font=("Arial", 32, "bold"), bg="black", fg="white")
        title_label.pack(pady=20)

        #subtítulo
        title_label2 = tk.Label(self.frame, text="Editar Time", font=("Arial", 18), bg="black", fg="white")
        title_label2.pack(pady=20)

        self.name_label = tk.Label(self.frame, text="Nome:")
        self.name_label.pack(pady=5)
        self.name_entry = tk.Entry(self.frame)
        self.name_entry.insert(0, self.team_data[1])
        self.name_entry.pack(pady=5)

        self.city_label = tk.Label(self.frame, text="Cidade:")
        self.city_label.pack(pady=5)
        self.city_entry = tk.Entry(self.frame)
        self.city_entry.insert(0, self.team_data[2])
        self.city_entry.pack(pady=5)

        self.stadium_label = tk.Label(self.frame, text="Estádio:")
        self.stadium_label.pack(pady=5)
        self.stadium_entry = tk.Entry(self.frame)
        self.stadium_entry.insert(0, self.team_data[3])
        self.stadium_entry.pack(pady=5)

        tk.Button(self.frame, text="Salvar", command=self.save_team).pack(pady=10)

        tk.Button(self.frame, text="Voltar", command=self.return_to_team_management_menu).pack(pady=10)

    def save_team(self):
        new_name = self.name_entry.get()
        new_city = self.city_entry.get()
        new_stadium = self.stadium_entry.get()

        if new_name and new_city and new_stadium:
            team_id = self.team_data[0]
            update_team_in_db(team_id, new_name, new_city, new_stadium)
            messagebox.showinfo("Sucesso", "Time atualizado com sucesso!")
            self.return_to_team_management_menu()
        else:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios. Preencha todos os campos e tente novamente.")

    def return_to_team_management_menu(self):
        from ui.frames.personalize.team_management_frame import TeamManagementFrame
        self.switch_frame(TeamManagementFrame)   
