import tkinter as tk
from persistence.database import create_tables
from ui.frames.main_menu_frame import MainMenuFrame
from ui.frames.personalize_menu_frame import PersonalizeMenuFrame
from ui.frames.personalize.team_management_frame import TeamManagementFrame
from ui.frames.personalize.team_add_frame import TeamAddFrame

class BruFootApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("BruFoot")

        # Maximizar a janela
        self.state('zoomed')

        self.frames = {}
        self.create_frames()
        self.show_frame(MainMenuFrame)

    def create_frames(self):      
        for F in (MainMenuFrame, PersonalizeMenuFrame, TeamManagementFrame, TeamAddFrame):
            frame = F(self, self.show_frame)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def show_frame(self, frame_class, **kwargs):
        frame = self.frames[frame_class]
        frame.on_show_frame(**kwargs)  # Chame o método on_show_frame
        frame.tkraise()

if __name__ == "__main__":
    create_tables()
    app = BruFootApp()
    app.mainloop()
