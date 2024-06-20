def incluir_titulo(tk, self, subtitulo):
    # Título
    title_label = tk.Label(self.frame, text="BruFoot", font=("Arial", 32, "bold"), bg="black", fg="white")
    title_label.pack(pady=20)

    # Subtítulo
    title_label2 = tk.Label(self.frame, text=subtitulo, font=("Arial", 18), bg="black", fg="white")
    title_label2.pack(pady=20)