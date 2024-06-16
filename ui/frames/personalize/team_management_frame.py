import tkinter as tk
from tkinter import ttk
from persistence.database import get_teams_from_db, delete_team_from_db
from ui.frames.base_frame import BaseFrame


class TeamManagementFrame(BaseFrame):
    def __init__(self, master, switch_frame):
        super().__init__(master, switch_frame)
        self.create_widgets()

    def create_widgets(self):
        #Título 
        title_label = tk.Label(self.frame, text="BruFoot", font=("Arial", 32, "bold"), bg="black", fg="white")
        title_label.pack(pady=20)

        #subtítulo
        title_label2 = tk.Label(self.frame, text="Times", font=("Arial", 18), bg="black", fg="white")
        title_label2.pack(pady=20)

        # Frame para Treeview e Scrollbar
        table_frame = tk.Frame(self.frame)
        table_frame.pack(pady=10, fill=tk.BOTH, expand=True)

        self.tree = ttk.Treeview(table_frame, columns=("id", "name", "city", "stadium"), show="headings")
        self.tree.heading("id", text="ID")
        self.tree.heading("name", text="Nome")
        self.tree.heading("city", text="Cidade")
        self.tree.heading("stadium", text="Estádio")

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
        tk.Button(self.frame, text="Criar Novo Time", command=self.add_team_menu).pack(pady=10)
        tk.Button(self.frame, text="Editar Time", command=self.edit_team).pack(pady=10)
        tk.Button(self.frame, text="Excluir Time", command=self.delete_team).pack(pady=10)
        tk.Button(self.frame, text="Voltar", command=self.return_to_personalize_menu).pack(pady=10)

    def return_to_personalize_menu(self):
        from ui.frames.personalize_menu_frame import PersonalizeMenuFrame
        self.switch_frame(PersonalizeMenuFrame)  

    def add_team_menu(self):
        from ui.frames.personalize.team_add_frame import TeamAddFrame
        self.switch_frame(TeamAddFrame)   

    def edit_team(self):
        selected_item = self.tree.selection()
        if selected_item:
            item = self.tree.item(selected_item)
            team_data = item['values']
            self.switch_frame_to_edit_team(team_data)
        else:
            tk.messagebox.showerror("Erro", "Nenhum time selecionado.")

    def switch_frame_to_edit_team(self, team_data):
        from ui.frames.personalize.team_edit_frame import TeamEditFrame
        frame = TeamEditFrame(self.master, self.switch_frame, team_data)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()

    def delete_team(self):
        selected_item = self.tree.selection()
        if selected_item:
            item = self.tree.item(selected_item)
            team_id = item['values'][0]  # A ID do time é a primeira coluna
            delete_team_from_db(team_id)
            self.update_teams_list()
        else:
            tk.messagebox.showerror("Erro", "Nenhum time selecionado.")

    def list_teams(self):
        teams = get_teams_from_db()
        # Limpar a tabela antes de preencher com os dados atualizados
        for item in self.tree.get_children():
            self.tree.delete(item)
        if not teams:
            self.tree.insert("", tk.END, values=("Não há registros.", "", ""))
        else:
            for team in teams:
                self.tree.insert("", tk.END, values=(team['id'], team['name'], team['city'], team['stadium']))

    def update_teams_list(self):
        self.list_teams()

    def on_show_frame(self):
        self.update_teams_list()
