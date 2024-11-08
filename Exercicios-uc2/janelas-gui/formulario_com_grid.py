'''
Formulário com tkinter seguindo o exemplo em: https://jocile.com/Programador/Python/Interface+grafica/Formulario-de-Entrada-de-Dados-com-Tkinter
'''

import tkinter as tk
from tkinter import ttk

# Criar a janela principal
window = tk.Tk()
window.title("Cadastro de Usuário")

# Criar um frame para conter os widgets do formulário
form_frame = ttk.Frame(window, padding="20")
form_frame.grid(row=0, column=0, sticky="nsew")

# Criar os widgets do formulário
nome_label = ttk.Label(form_frame, text="Nome:")
nome_entry = ttk.Entry(form_frame)

email_label = ttk.Label(form_frame, text="Email:")
email_entry = ttk.Entry(form_frame)

senha_label = ttk.Label(form_frame, text="Senha:")
senha_entry = ttk.Entry(form_frame, show="*")

# Organizar os widgets usando o gerenciador de layout grid
nome_label.grid(row=0, column=0, sticky="w")
nome_entry.grid(row=0, column=1, sticky="ew")

email_label.grid(row=1, column=0, sticky="w")
email_entry.grid(row=1, column=1, sticky="ew")

senha_label.grid(row=2, column=0, sticky="w")
senha_entry.grid(row=2, column=1, sticky="ew")

# Criar um botão para enviar o formulário
enviar_button = ttk.Button(form_frame, text="Enviar")
enviar_button.grid(row=3, column=0, columnspan=2, pady="10")

# Iniciar o loop de eventos
window.mainloop()