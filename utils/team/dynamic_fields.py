import tkinter as tk
from utils.team.colors import choose_color, update_color_preview
from persistence.config import TEAM_ATTRIBUTES
from utils.team.create_team_validation import validate_integer, validate_initial_level

def create_validation_commands(master):
    vcmd_integer = (master.register(validate_integer), '%P')
    vcmd_initial_level = (master.register(validate_initial_level), '%P')
    return vcmd_integer, vcmd_initial_level

def create_dynamic_fields(frame, entries, master, update_color_preview_func):
    vcmd_integer, vcmd_initial_level = create_validation_commands(master)

    for attribute in TEAM_ATTRIBUTES:
        label_text = attribute[3]
        field_frame = tk.Frame(frame, bg="black")
        field_frame.pack(pady=5, fill="x")

        label = tk.Label(field_frame, text=f"{label_text}:", bg="black", fg="white")
        label.pack(side="left", padx=5)

        if attribute[0] == "initial_level":
            entry = tk.Entry(field_frame, validate="key", validatecommand=vcmd_initial_level)
        elif attribute[1] == "INTEGER":
            entry = tk.Entry(field_frame, validate="key", validatecommand=vcmd_integer)
        elif "color" in attribute[0]:
            button = tk.Button(
                field_frame, 
                text="Escolher Cor", 
                command=lambda key=attribute[0]: choose_color(entries, key, update_color_preview_func)
            )
            button.pack(side="left", padx=5, fill="x", expand=True)
            entry = tk.Entry(field_frame)
        else:
            entry = tk.Entry(field_frame)

        entry.pack(side="left", padx=5, fill="x", expand=True)
        entries[attribute[0]] = entry

        if attribute[0] == "name":
            entry.bind("<KeyRelease>", lambda event, key=attribute[0]: update_color_preview_func())
