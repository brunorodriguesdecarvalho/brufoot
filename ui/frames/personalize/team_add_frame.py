import tkinter as tk
from tkinter import colorchooser
from persistence.team_dao import add_team_to_db
from tkinter import messagebox
from ui.frames.base_frame import BaseFrame
from persistence.config import TEAM_ATTRIBUTES

class TeamAddFrame(BaseFrame):
    def __init__(self, master, switch_frame):
        super().__init__(master, switch_frame)
        self.entries = {}
        self.create_widgets()

    def create_widgets(self):
        # Função de validação para entradas inteiras
        def validate_integer(P):
            if P.isdigit() or P == "":
                return True
            return False
        
        def validate_initial_level(P):
            if P.isdigit() and 0 <= int(P) <= 100:
                return True
            return False
        
        vcmd_integer = (self.master.register(validate_integer), '%P')
        vcmd_initial_level = (self.master.register(validate_initial_level), '%P')

        # Título
        title_label = tk.Label(self.frame, text="BruFoot", font=("Arial", 32, "bold"), bg="black", fg="white")
        title_label.pack(pady=20)

        # Subtítulo
        title_label2 = tk.Label(self.frame, text="Adicionar Time", font=("Arial", 18), bg="black", fg="white")
        title_label2.pack(pady=20)

        # Aviso de campos requeridos
        required_label = tk.Label(self.frame, text="Campos Obrigatórios", font=("Arial", 10, "italic"), bg="black", fg="white")
        required_label.pack(pady=20)

        # Gerar campos dinamicamente
        for attribute in TEAM_ATTRIBUTES:
            label_text = attribute[3]
            field_frame = tk.Frame(self.frame, bg="black")
            field_frame.pack(pady=5, fill="x")

            label = tk.Label(field_frame, text=f"{label_text}:", bg="black", fg="white")
            label.pack(side="left", padx=5)

            if attribute[0] == "initial_level":
                entry = tk.Entry(field_frame, validate="key", validatecommand=vcmd_initial_level)
                entry.pack(side="left", padx=5, fill="x", expand=True)
            elif attribute[1] == "INTEGER":
                entry = tk.Entry(field_frame, validate="key", validatecommand=vcmd_integer)
                entry.pack(side="left", padx=5, fill="x", expand=True)
            elif "color" in attribute[0]:
                button = tk.Button(
                    field_frame, 
                    text="Escolher Cor", 
                    command=lambda key=attribute[0]: self.choose_color(key)
                )
                button.pack(side="left", padx=5, fill="x", expand=True)
                entry = tk.Entry(field_frame)
                entry.pack(side="left", padx=5, fill="x", expand=True)
            else:
                entry = tk.Entry(field_frame)
                entry.pack(side="left", padx=5, fill="x", expand=True)
            
            self.entries[attribute[0]] = entry

            if attribute[0] == "name":
                entry.bind("<KeyRelease>", lambda event, key=attribute[0]: self.update_color_preview())

        # Canvas para pré-visualização das cores
        self.preview_canvas = tk.Canvas(
            self.frame, 
            width=300, 
            height=50, 
            bg="white"
        )

        self.preview_canvas.pack(pady=20)

        self.preview_text = self.preview_canvas.create_text(
            150,
            25,
            text="",
            font=("Arial", 14),
            fill="black"
        )


        # Botões
        button_frame = tk.Frame(self.frame, bg="black")
        button_frame.pack(pady=20)

        tk.Button(button_frame, text="Salvar", command=self.save_team).pack(side="left", padx=5)
        tk.Button(button_frame, text="Voltar", command=self.return_to_team_management_menu).pack(side="left", padx=5)

    def return_to_team_management_menu(self):
        from ui.frames.personalize.team_management_frame import TeamManagementFrame
        self.switch_frame(TeamManagementFrame)    

    def choose_color(self, key):
        color_code = colorchooser.askcolor(title="Escolha uma cor")[1]
        if color_code:
            self.entries[key].delete(0, tk.END)
            self.entries[key].insert(0, color_code)
            self.update_color_preview()

    def update_color_preview(self):
        primary_color = self.entries.get("primary_color").get()
        secondary_color = self.entries.get("secondary_color").get()
        team_name = self.entries.get("name").get()

        if primary_color:
            self.preview_canvas.configure(bg=primary_color)
        if team_name:
            self.preview_canvas.itemconfig(
                self.preview_text, 
                text=f"{team_name}", 
            )
        if secondary_color:
            self.preview_canvas.itemconfig(
                self.preview_text, 
                fill=secondary_color
            )
        else:
            self.preview_canvas.itemconfig(self.preview_text, f"{team_name}", fill="black")

    def save_team(self):
        team_data = {key: entry.get() for key, entry in self.entries.items()}
        missing_fields = [attr[0] for attr in TEAM_ATTRIBUTES if not team_data[attr[0]] and "NOT NULL" in attr[2]]
        
        if not missing_fields:
            add_team_to_db(**team_data)
            messagebox.showinfo("Sucesso", "Time adicionado com sucesso!")
            self.return_to_team_management_menu()
        else:
            messagebox.showerror(
                "Erro", 
                "Todos os campos obrigatórios devem ser preenchidos. Tente novamente, por favor."
            )
