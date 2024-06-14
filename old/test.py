import tkinter as tk
import random

class Time:
    def __init__(self, nome):
        self.nome = nome
        self.pontos = 0
        self.saldo_gols = 0

def simular_jogo(time_a, time_b):
    gols_time_a = random.randint(0, 5)
    gols_time_b = random.randint(0, 5)
    time_a.saldo_gols += gols_time_a - gols_time_b
    time_b.saldo_gols += gols_time_b - gols_time_a
    if gols_time_a > gols_time_b:
        time_a.pontos += 3
    elif gols_time_b > gols_time_a:
        time_b.pontos += 3
    else:
        time_a.pontos += 1
        time_b.pontos += 1

def simular_campeonato():
    times = [Time("Time A"), Time("Time B"), Time("Time C"), Time("Time D")]

    for i in range(len(times)):
        for j in range(i + 1, len(times)):
            simular_jogo(times[i], times[j])

    return sorted(times, key=lambda x: (x.pontos, x.saldo_gols), reverse=True)

def exibir_classificacao(times):
    for i, time in enumerate(times):
        label = tk.Label(root, text=f"{i+1}. {time.nome} - Pontos: {time.pontos} | Saldo de Gols: {time.saldo_gols}")
        label.pack()

def reiniciar():
    for widget in root.winfo_children():
        widget.destroy()
    iniciar_simulacao()

def iniciar_simulacao():
    times = simular_campeonato()
    exibir_classificacao(times)
    reiniciar_button = tk.Button(root, text="Reiniciar", command=reiniciar)
    reiniciar_button.pack()

root = tk.Tk()
root.title("Simulador de Campeonato")

iniciar_simulacao()

root.mainloop()
