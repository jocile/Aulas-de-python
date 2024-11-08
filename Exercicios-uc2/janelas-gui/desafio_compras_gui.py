'''
Formulário com tkinter seguindo o exemplo em: https://jocile.com/Programador/Python/Interface+grafica/Formulario-de-Entrada-de-Dados-com-Tkinter

Algoritmo:

- [X] Fase estruturada 
- [X] Organize os código em funções.
- [X] Nova fase criando uma interface gráfica 
  - Criando uma janela para o aplicativo
- [ ] Crie uma função para salvar a lista e o total em um arquivo txt.
- [ ] Crie uma nova opção no menu para salvar a lista.
- [ ] Nova fase criando a lista de produtos (CRUD) 
- [ ] Criar uma lista de produtos e salvar em arquivo txt
- [ ] Carregar a lista de produtos de um arquivo txt;
- [ ] Atualizar a lista adicionando novos produtos;
- [ ] Deletar um produto da lista
- [ ] Criando um menu de opções na janela
'''

import tkinter as tk
from tkinter import ttk

produtos = {'Arroz': 5.90, 
            'Macarrão': 3.60,
            'Feijão': 8.50,
            'Carne': 50.90,
            'Frango':20.00,}

# Função para atualizar a lista de produtos
def atualizar_lista():
  carrinho_listbox.insert(tk.END, produtos_combobox.get())
  preco_listbox.insert(tk.END, produtos[produtos_combobox.get()])
  atualizar_total()

# Função para limpar a lista de produtos
def limpar_lista():
    produtos_combobox.config(values=list(produtos.keys()))
    carrinho_listbox.delete(0, tk.END)
    preco_listbox.delete(0, tk.END)
    atualizar_total()

# Função para atualizar o total
def atualizar_total():
    total = sum(produtos[produto] for produto in carrinho_listbox.get(0, tk.END))
    total_label.config(text=f"Total: R$ {total:.2f}")

# Criar a janela principal
window = tk.Tk()
window.title("Cadastro de Usuário")

# Criar um frame para conter os widgets do formulário
frame = tk.Frame(window)
frame.pack()

# Frame de produtos
produtos_frame = tk.LabelFrame(frame, text="Lista de Produtos")
produtos_frame.grid(row=0, column=0, padx=20, pady=10)

produto_label = tk.Label(produtos_frame, text="Produtos:")
produto_label.grid(row=0, column=0)

valor_label = tk.Label(produtos_frame, text="Valor:")
valor_label.grid(row=0, column=1)

produtos_combobox = ttk.Combobox(produtos_frame, values=list(produtos.keys()))
produtos_combobox.grid(row=1, column=0)

r_label = tk.Label(produtos_frame, text="R$")
r_label.grid(row=1, column=1)

preco_label = tk.Label(produtos_frame, text="")
preco_label.grid(row=1, column=2)

produtos_combobox.bind("<<ComboboxSelected>>", lambda event: preco_label.config(text=produtos[produtos_combobox.get()]))

botao_adicionar = tk.Button(produtos_frame, text="Adicionar ao Carrinho", command=atualizar_lista)
botao_adicionar.grid(row=2, column=0)

# Frame do carinho de compras
carrinho_frame = tk.LabelFrame(frame, text="Carrinho de Compras")
carrinho_frame.grid(row=1, column=0, padx=20, pady=10)

carrinho_label = tk.Label(carrinho_frame, text="Produtos:")
carrinho_label.grid(row=0, column=0)

carrinho_listbox = tk.Listbox(carrinho_frame, width=20)
carrinho_listbox.grid(row=1, column=0)

precos_label = tk.Label(carrinho_frame, text="Preços:")
precos_label.grid(row=0, column=1)

preco_listbox = tk.Listbox(carrinho_frame, width=10)
preco_listbox.grid(row=1, column=1)

total_label = tk.Label(carrinho_frame, text="Total:")
total_label.grid(row=2, column=1)

window.mainloop()