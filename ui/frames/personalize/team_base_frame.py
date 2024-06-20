import tkinter as tk
from ui.frames.base_frame import BaseFrame
from utils.titulo import incluir_titulo
from utils.team.dynamic_fields import create_dynamic_fields
from utils.team.colors import update_color_preview, create_color_preview

class BaseTeamFrame(BaseFrame):
    def __init__(self, master, switch_frame, title):
        super().__init__(master, switch_frame)
        self.entries = {}
        self.title = title
        self.create_widgets()
        self.populate_default_values()

    def create_widgets(self):
        incluir_titulo(tk, self, self.title)
        self.create_required_label()
        self.create_dynamic_fields()
        self.create_color_preview()
        self.create_buttons()

    def create_required_label(self):
        required_label = tk.Label(
            self.frame, 
            text="Campos Obrigatórios", 
            font=("Arial", 10, "italic"), 
            bg="black", 
            fg="white"
        )
        required_label.pack(pady=20)

    def create_dynamic_fields(self):
        create_dynamic_fields(self.frame, self.entries, self.master, self.update_color_preview)

    def create_color_preview(self):
        self.preview_canvas, self.preview_text = create_color_preview(self.frame)

    def create_buttons(self):
        button_frame = tk.Frame(self.frame, bg="black")
        button_frame.pack(pady=20)

        tk.Button(
            button_frame, 
            text="Salvar", 
            command=self.save_team
        ).pack(side="left", padx=5)

        tk.Button(
            button_frame, 
            text="Voltar", 
            command=self.return_to_team_management_menu
        ).pack(side="left", padx=5)

    def return_to_team_management_menu(self):
        from ui.frames.personalize.team_management_frame import TeamManagementFrame
        self.switch_frame(TeamManagementFrame)

    def update_color_preview(self):
        update_color_preview(self.entries, self.preview_canvas, self.preview_text)

    def save_team(self):
        pass  # to be implemented in child classes

    def populate_default_values(self):
        # Populate default values
        self.entries.get("primary_color").insert(0, "#000000")
        self.entries.get("secondary_color").insert(0, "#FFFFFF")
        self.entries.get("name").insert(0, "Nome do Time")
        self.update_color_preview()