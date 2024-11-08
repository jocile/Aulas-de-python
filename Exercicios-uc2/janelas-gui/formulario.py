'''
Formulário com tkinter seguindo o exemplo em: https://jocile.com/Programador/Python/Interface+grafica/Formulario-de-Entrada-de-Dados-com-Tkinter
'''

import tkinter as tk

def enviar_dados():
  nome = nome_entry.get()
  idade = idade_spinbox.get()
  print(f"Nome: {nome}, Idade: {idade}")

window = tk.Tk()
window.title("Formulário de Entrada")

nome_label = tk.Label(window, text="Nome:")
nome_label.grid(row=0, column=0)

nome_entry = tk.Entry(window)
nome_entry.grid(row=0, column=1)

idade_label = tk.Label(window, text="Idade:")
idade_label.grid(row=1, column=0)

idade_spinbox = tk.Spinbox(window, from_=18, to=100)
idade_spinbox.grid(row=1, column=1)

enviar_button = tk.Button(window, text="Enviar", command=enviar_dados)
enviar_button.grid(row=2, column=0, columnspan=2)

window.mainloop()