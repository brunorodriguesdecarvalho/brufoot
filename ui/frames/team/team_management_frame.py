import tkinter as tk
from tkinter import ttk
from ui.frames.base_frame import BaseFrame
from persistence.config import TEAM_ATTRIBUTES
from utils.titulo import incluir_titulo
from utils.team.list_teams import list_teams
from utils.team.delete_team import delete_team
from utils.team.edit_team import edit_team

class TeamManagementFrame(BaseFrame):
    
    def __init__(self, master, switch_frame):
        super().__init__(master, switch_frame)
        self.team_ids = []
        self.create_widgets()

    def create_widgets(self):
        
        incluir_titulo(tk, self, "Times Cadastrados")

        # Frame para Treeview e Scrollbar
        table_frame = tk.Frame(self.frame)
        table_frame.pack(pady=10, fill=tk.BOTH, expand=True)

        columns = tuple(attr[0] for attr in TEAM_ATTRIBUTES)
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings")

        for attr in TEAM_ATTRIBUTES:
            self.tree.heading(attr[0], text=attr[3])

        # Scrollbars
        scrollbar_y = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=self.tree.yview)
        scrollbar_x = ttk.Scrollbar(table_frame, orient=tk.HORIZONTAL, command=self.tree.xview)
        self.tree.configure(yscroll=scrollbar_y.set, xscroll=scrollbar_x.set)

        # Posicionar Treeview e Scrollbars
        self.tree.grid(row=0, column=0, sticky='nsew')
        scrollbar_y.grid(row=0, column=1, sticky='ns')
        scrollbar_x.grid(row=1, column=0, sticky='ew')

        table_frame.grid_rowconfigure(0, weight=1)
        table_frame.grid_columnconfigure(0, weight=1)

        # Botões
        tk.Button(
            self.frame, 
            text="Criar Novo Time", 
            command=self.add_team_menu
            ).pack(pady=10)
        
        tk.Button(
            self.frame, 
            text="Editar Time", 
            command=lambda: edit_team(
                self.tree, 
                self.team_ids, 
                self.switch_frame_to_edit_team
            )
        ).pack(pady=10)

        tk.Button(
            self.frame, 
            text="Excluir Time", 
            command=lambda: delete_team(
                self.tree, 
                self.team_ids, 
                self.update_teams_list
            )
        ).pack(pady=10)

        tk.Button(
            self.frame, 
            text="Voltar", 
            command=self.return_to_personalize_menu
        ).pack(pady=10)

    def return_to_personalize_menu(self):
        from ui.frames.personalize_menu_frame import PersonalizeMenuFrame
        self.switch_frame(PersonalizeMenuFrame)  

    def add_team_menu(self):
        from ui.frames.team.team_add_frame import TeamAddFrame
        self.switch_frame(TeamAddFrame)   

    def switch_frame_to_edit_team(self, team_data, team_id):
        from ui.frames.team.team_edit_frame import TeamEditFrame
        frame = TeamEditFrame(self.master, self.switch_frame, team_data, team_id)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()

    def update_teams_list(self):
        list_teams(self, tk)

    def on_show_frame(self):
        self.update_teams_list()
