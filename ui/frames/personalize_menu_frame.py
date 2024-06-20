import tkinter as tk
from tkinter import messagebox
from ui.frames.base_frame import BaseFrame
from utils.titulo import incluir_titulo

class PersonalizeMenuFrame(BaseFrame):
    def __init__(self, master, switch_frame):
        super().__init__(master, switch_frame)
        self.create_widgets()

    def create_widgets(self):

        incluir_titulo(tk, self, "Menu de Edição")

        tk.Button(self.frame, text="Times", command=self.open_team_management).pack(pady=10)
        tk.Button(self.frame, text="Jogadores", command=self.not_implemented).pack(pady=10)
        tk.Button(self.frame, text="Campeonatos", command=self.not_implemented).pack(pady=10)
        tk.Button(self.frame, text="Estádios", command=self.not_implemented).pack(pady=10)
        tk.Button(self.frame, text="Voltar", command=self.return_to_main_menu).pack(pady=10)

    def not_implemented(self):
        messagebox.showinfo("Info", "Funcionalidade ainda não implementada")

    def open_team_management(self):
        from ui.frames.team.team_management_frame import TeamManagementFrame
        self.switch_frame(TeamManagementFrame)

    def return_to_main_menu(self):
        from ui.frames.main_menu_frame import MainMenuFrame
        self.switch_frame(MainMenuFrame)

