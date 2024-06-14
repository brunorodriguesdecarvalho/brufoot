import tkinter as tk
from tkinter import messagebox

# Lista de times de São Paulo (inicialmente vazia)
times_sp = []

# Função para adicionar um time à lista
def adicionar_time():
    nome_time = entry_nome.get()
    if nome_time:
        times_sp.append(nome_time)
        atualizar_lista_times()
        limpar_campos()
    else:
        messagebox.showwarning("Erro", "Por favor, insira um nome para o time.")

# Função para editar um time da lista
def editar_time():
    indice = listbox_times.curselection()
    if indice:
        nome_time = entry_nome.get()
        if nome_time:
            times_sp[indice[0]] = nome_time
            atualizar_lista_times()
            limpar_campos()
        else:
            messagebox.showwarning("Erro", "Por favor, insira um nome para o time.")
    else:
        messagebox.showwarning("Erro", "Por favor, selecione um time para editar.")

# Função para excluir um time da lista
def excluir_time():
    indice = listbox_times.curselection()
    if indice:
        times_sp.pop(indice[0])
        atualizar_lista_times()
        limpar_campos()
    else:
        messagebox.showwarning("Erro", "Por favor, selecione um time para excluir.")

# Função para atualizar a lista de times na interface
def atualizar_lista_times():
    listbox_times.delete(0, tk.END)
    for time in times_sp:
        listbox_times.insert(tk.END, time)

# Função para limpar os campos de entrada
def limpar_campos():
    entry_nome.delete(0, tk.END)

# Criar janela principal
root = tk.Tk()
root.title("CRUD de Times")

# Criar campos de entrada e botões
label_nome = tk.Label(root, text="Nome do Time:")
label_nome.pack()

entry_nome = tk.Entry(root)
entry_nome.pack()

button_adicionar = tk.Button(root, text="Adicionar", command=adicionar_time)
button_adicionar.pack()

button_editar = tk.Button(root, text="Editar", command=editar_time)
button_editar.pack()

button_excluir = tk.Button(root, text="Excluir", command=excluir_time)
button_excluir.pack()

listbox_times = tk.Listbox(root)
listbox_times.pack()

# Atualizar lista de times
atualizar_lista_times()

root.mainloop()
