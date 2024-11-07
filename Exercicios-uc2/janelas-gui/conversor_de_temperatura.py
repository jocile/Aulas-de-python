'''
Criando um conversor de temperatura em Python com Tkinter
- [X] Criando uma janela com Tkinter
- [X] Criando um frame para a entrada de dados
- [X] Criando um entry para a entrada de dados
- [X] Criando um frame para o botão
- [X] Criando um label para o botão
- [X] Criar a função para conversão
- [X] Criar o comando para o botão
'''

import tkinter as tk


font_padrao = ["Arial", 20]
def fahrenheit_to_celsius():
    """Convert the value for Fahrenheit to Celsius and insert the
    result into lbl_result.
    """
    fahrenheit = entrada.get()
    celsius = (5 / 9) * (float(fahrenheit) - 32)
    lbl_resultado["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"

window = tk.Tk()
window.title("Conversor de temperatura")
window.geometry("420x140")

frame1 = tk.Frame(master=window, width=150, height=100)
frame1.pack(side=tk.LEFT, expand=True)
entrada = tk.Entry(master=frame1, font= font_padrao, width=8)
entrada.pack(side=tk.LEFT, expand=True, padx=10, pady=40)

frame2 = tk.Frame(master=window)
frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
lblF = tk.Label(master=frame2, text="°F", font= font_padrao)
lblF.pack(fill=tk.BOTH, side=tk.LEFT, expand=True, padx=10, pady=10)

frame3 = tk.Frame(master=window, width=50)
frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
botao = tk.Button(
  master=frame3, 
  text="➡", 
  font= font_padrao,
  command=fahrenheit_to_celsius
  )
botao.pack(fill=tk.BOTH, side=tk.LEFT, expand=True, padx=10, pady=40)

frame4 = tk.Frame(master=window)
frame4.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
lbl_resultado = tk.Label(master=frame4, text="°C", font= font_padrao)
lbl_resultado.pack(fill=tk.BOTH, side=tk.LEFT, expand=True, padx=10, pady=10)


window.mainloop()