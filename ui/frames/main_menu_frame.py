import tkinter as tk
from tkinter import messagebox
from ui.frames.base_frame import BaseFrame
from utils.titulo import incluir_titulo

class MainMenuFrame(BaseFrame):
    def __init__(self, master, switch_frame):
        super().__init__(master, switch_frame)
        self.create_widgets()

    def create_widgets(self):
        
        incluir_titulo(tk, self, "Menu Principal")

        tk.Button(self.frame, text="Jogar", command=self.play_game).pack(pady=10)
        tk.Button(self.frame, text="Editar", command=self.open_personalize_menu).pack(pady=10)
        tk.Button(self.frame, text="Sair", command=self.quit).pack(pady=10)
    
    def play_game(self):
        messagebox.showinfo("Info", "Funcionalidade de jogar ainda não implementada")

    def open_personalize_menu(self):
        from ui.frames.personalize_menu_frame import PersonalizeMenuFrame
        self.switch_frame(PersonalizeMenuFrame)