import tkinter as tk

# Criando a janela principal
root = tk.Tk()
root.title("Testando Tkinter")
root.geometry("500x400")  # Ajuste no tamanho da janela

# Saudação inicial
greeting_label = tk.Label(
    root,
    text="Bem vindo!",
    fg="white",
    bg="darkblue",
    font=("Helvetica", 16, "bold"),
    width=30,
    height=2
)
greeting_label.pack(pady=20)  # Espaço entre o label e o resto dos widgets

# Entrada de texto
entry = tk.Entry(
    root,
    fg="black",
    bg="lightyellow",
    font=("Arial", 14),
    width=40
)
entry.pack(pady=10)

# Função do botão
def on_button_click():
    input_text = entry.get()
    # Exibir mensagem de saudação no console
    print(f"Botão clicado! O texto digitado: {input_text}")
    greeting_label.config(text=f"E ai, {input_text}!")  # Atualiza o label com o nome inserido

# Criação do botão
button = tk.Button(
    root,
    text="Clique logo",
    font=("Arial", 14),
    bg="green",
    fg="white",
    command=on_button_click
)
button.pack(pady=20)  # Espaço entre o botão e outros widgets

# Área de resultado
result_area = tk.Label(
    root,
    text="Digite seu nome e clique no botão",
    fg="black",
    bg="lightgray",
    font=("Arial", 12),
    width=50,
    height=4
)
result_area.pack(pady=10)

# Controle para o loop principal da interface gráfica
root.mainloop()