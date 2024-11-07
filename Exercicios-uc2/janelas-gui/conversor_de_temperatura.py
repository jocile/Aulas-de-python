'''
Criando um conversor de temperatura em Python com Tkinter
- [X] Criando uma janela com Tkinter
- [X] Criando um frame para a entrada de dados
- [X] Criando um entry para a entrada de dados
- [X] Criando um frame para o botão
- [X] Criando um label para o botão
- [ ] Criar a função para conversão
- [ ] Criar o comando para o botão
'''

import tkinter as tk

window = tk.Tk()
window.title("Conversor de temperatura")
window.geometry("420x140")

frame1 = tk.Frame(master=window, width=150, height=100)
frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
entrada = tk.Entry(master=frame1)
entrada.pack(fill=tk.BOTH, side=tk.LEFT, expand=True, padx=10, pady=40)

frame2 = tk.Frame(master=window)
frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
lblF = tk.Label(master=frame2, text="°F", font=("Arial", 20))
lblF.pack(fill=tk.BOTH, side=tk.LEFT, expand=True, padx=10, pady=10)

frame3 = tk.Frame(master=window, width=50)
frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
botao = tk.Button(master=frame3, text="➡", font=("Arial", 25))
botao.pack(fill=tk.BOTH, side=tk.LEFT, expand=True, padx=10, pady=40)

frame4 = tk.Frame(master=window)
frame4.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
lblC = tk.Label(master=frame4, text="°C", font=("Arial", 20))
lblC.pack(fill=tk.BOTH, side=tk.LEFT, expand=True, padx=10, pady=10)


window.mainloop()