'''
Criado a partir do tutorial https://realpython.com/python-gui-tkinter/
'''

import tkinter as tk

# Criação da janela principal
janela = tk.Tk()
janela.title("Minha Primeira Janela")
janela.geometry("300x300")

# Criação de um rótulo
greeting = tk.Label(text="Usando a Interface Gráfica Tkinter",
                    fg="white",  # Set the text color to white
                    bg="black",  # Set the background color to black
                    width=30,
                    height=5
                    )
greeting.pack(pady=10)

# label = tk.Label(janela, text="Olá, Tkinter!")
# label.pack()

# Criação de um botão
button = tk.Button(janela,
                   text="Clique Aqui",
                   fg="yellow",
                    bg="blue",
                    width=15,
                    height=2,
                    command=lambda: greeting.config(text="Botão clicado!")
                   )
button.pack(pady=10)

# Adicionando uma entrada de texto
entry = tk.Entry(fg="yellow", bg="blue", width=50)
entry.pack(pady=10)

button2 = tk.Button(text="Escreva algo e clique no botão",
                    command=lambda: greeting.config(text=entry.get()),
                    fg="yellow",
                    bg="blue",
                   )
button2.pack(pady=10)
 
button3 = tk.Button(text="Apagar",
                    command=lambda: greeting.config(text=""),
                    fg="yellow",
                    bg="blue",
                   )
button3.pack(pady=10)
 
# Iniciando o loop principal
janela.mainloop()