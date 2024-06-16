import tkinter as tk
from persistence.database import add_team_to_db
from tkinter import messagebox
from ui.frames.base_frame import BaseFrame

class TeamAddFrame(BaseFrame):
    def __init__(self, master, switch_frame):
        super().__init__(master, switch_frame)
        self.create_widgets()

    def create_widgets(self):

        #Título 
        title_label = tk.Label(self.frame, text="BruFoot", font=("Arial", 32, "bold"), bg="black", fg="white")
        title_label.pack(pady=20)

        #subtítulo
        title_label2 = tk.Label(self.frame, text="Adicionar Time", font=("Arial", 18), bg="black", fg="white")
        title_label2.pack(pady=20)

        self.entry_name = tk.Entry(self.frame)
        tk.Label(self.frame, text="Nome:", bg="black", fg="white").pack(pady=5)
        self.entry_name.pack(pady=5)

        self.entry_city = tk.Entry(self.frame)
        tk.Label(self.frame, text="Cidade:", bg="black", fg="white").pack(pady=5)
        self.entry_city.pack(pady=5)

        self.entry_stadium = tk.Entry(self.frame)
        tk.Label(self.frame, text="Estádio:", bg="black", fg="white").pack(pady=5)
        self.entry_stadium.pack(pady=5)


        tk.Button(self.frame, text="Salvar", command=self.save_team).pack(pady=20)

        tk.Button(self.frame, text="Voltar", command=self.return_to_team_management_menu).pack(pady=10)

    def return_to_team_management_menu(self):
        from ui.frames.personalize.team_management_frame import TeamManagementFrame
        self.switch_frame(TeamManagementFrame)    

    def save_team(self):
        name = self.entry_name.get()
        city = self.entry_city.get()
        stadium = self.entry_stadium.get()
        if name and city and stadium:
            add_team_to_db(name, city, stadium)
            messagebox.showinfo("Sucesso", "Time adicionado com sucesso!")
            self.return_to_team_management_menu()
        else:
            messagebox.showerror("Erro", "Todos os campos são mandatórios. Tente novamente, por favor.")



