from tkinter import colorchooser
import tkinter as tk

def choose_color(entries, key, update_preview_callback):
    color_code = colorchooser.askcolor(title="Escolha uma cor")[1]
    if color_code:
        entries[key].delete(0, "end")
        entries[key].insert(0, color_code)
        update_preview_callback()

def update_color_preview(entries, canvas, text_item):
    primary_color = entries.get("primary_color").get()
    secondary_color = entries.get("secondary_color").get()
    team_name = entries.get("name").get()

    if primary_color:
        canvas.configure(bg=primary_color)
    if team_name:
        canvas.itemconfig(text_item, text=f"{team_name}")
    if secondary_color:
        canvas.itemconfig(text_item, fill=secondary_color)
    else:
        canvas.itemconfig(text_item, fill="black")

def create_color_preview(frame):
    preview_canvas = tk.Canvas(
        frame, 
        width=300, 
        height=50, 
        bg="white"
    )
    preview_canvas.pack(pady=20)
    preview_text = preview_canvas.create_text(
        150,
        25,
        text="Example Team",
        font=("Arial", 14),
        fill="black"
    )
    return preview_canvas, preview_text
