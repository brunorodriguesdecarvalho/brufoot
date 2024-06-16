import tkinter as tk
from PIL import Image, ImageTk

class BaseFrame(tk.Frame):
    def __init__(self, master, switch_frame, bg_color="black", bg_image="assets/logo.jpg", **kwargs):
        super().__init__(master, bg=bg_color, **kwargs)
        self.switch_frame = switch_frame
        self.master = master
        self.bg_color = bg_color
        self.bg_image = bg_image
        self.create_container()
        if self.bg_image:
            self.set_background_image()

    def create_container(self):
        self.container = tk.Frame(self, bg=self.bg_color)
        self.container.pack(expand=True, fill=tk.BOTH)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        self.frame = tk.Frame(self.container, bg=self.bg_color)
        self.frame.grid(row=0, column=0)

    def set_background_image(self):
        bg_image = Image.open(self.bg_image)
        self.bg_image = ImageTk.PhotoImage(bg_image)
        bg_label = tk.Label(self.container, image=self.bg_image, bg=self.bg_color)
        bg_label.image = self.bg_image  # Keep a reference to avoid garbage collection
        bg_label.place(relwidth=1, relheight=1)
        bg_label.lower()

    def on_show_frame(self, **kwargs):
        """ This method is called when the frame is shown """
        pass

    def switch_frame(self, new_frame_class, **kwargs):
        new_frame = new_frame_class(self.master, self.switch_frame, **kwargs)
        self.master.switch_frame(new_frame)
