'''
Repositório do Marvin:
https://github.com/MarvinTL-24/Marvin-Python/blob/main/desafios/Carrinho/Lista.py
'''

import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3

'''
[]Criar banco de dados.
[]Criar criar as funções principais.
[]Inserir os dados das funções no banco.
[]Manter as funções anteriores com desconto,total e novo valor.
[]Criar a interface de acordo com as anteriores.
[]Criar um local para visualizar
[]Criar um selecionar item.
[]Avançar pra editar o item selecionando.
[]Criar um selecionar item para deletar seguindo os passos anteriores.
[]Selecionar e apagar tudo de uma vez.
[]Criar um limpador de entradas.
[]Redimensionar a janela e melhorar o estilo de visualização.
OBS: Não é necessario a criação de classes, pois só é necessario um unico banco de dados com esses 3 itens; logo só funções já são o suficiente.
'''


# Funções para interagir com o banco de dados
def criar_banco():
    conn = sqlite3.connect('compras.db')
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS lista_Produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        quantidade INTEGER NOT NULL,
        valor REAL NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

def adicionar_item_db(nome, quantidade, valor):
    conn = sqlite3.connect('compras.db')
    c = conn.cursor()
    c.execute('INSERT INTO lista_Produtos (nome, quantidade, valor) VALUES (?, ?, ?)', (nome, quantidade, valor))
    conn.commit()
    conn.close()

def editar_item_db(item_id, nome, quantidade, valor):
    conn = sqlite3.connect('compras.db')
    c = conn.cursor()
    c.execute('UPDATE lista_Produtos SET nome = ?, quantidade = ?, valor = ? WHERE id = ?', (nome, quantidade, valor, item_id))
    conn.commit()
    conn.close()

def deletar_item_db(item_id):
    conn = sqlite3.connect('compras.db')
    c = conn.cursor()
    c.execute('DELETE FROM lista_Produtos WHERE id = ?', (item_id,))
    conn.commit()
    conn.close()

def obter_itens_db():
    conn = sqlite3.connect('compras.db')
    c = conn.cursor()
    c.execute('SELECT * FROM lista_Produtos')
    itens = c.fetchall()
    conn.close()
    return itens

# Função de interface para adicionar item
def adicionar_itens_gui():
    item = entry_item.get()
    try:
        quantidade = int(entry_quantidade.get())
        valor = float(entry_valor.get())
        
        if item and quantidade > 0 and valor > 0:
            adicionar_item_db(item, quantidade, valor)
            listar_itens_gui()
            limpar_entradas()
        else:
            messagebox.showerror("Erro", "Nos espaços de quantidade e valor deve-se por valores positivos e reais!")
    except ValueError:
        messagebox.showerror("Erro", "Quantidade deve ser um número inteiro e Valor um número válido!")

# Função de interface para editar item
def editar_itens_gui():
    try:
        selecionado = listbox_itens.curselection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecionar um item para editar!")
            return
        
        item_id = listbox_itens.get(selecionado[0]).split()[0]
        item_id = int(item_id)
        
        nome = entry_item.get()
        quantidade = int(entry_quantidade.get())
        valor = float(entry_valor.get())

        editar_item_db(item_id, nome, quantidade, valor)
        listar_itens_gui()
        limpar_entradas()
    except ValueError:
        messagebox.showerror("Erro", "Preencha corretamente os campos de quantidade e valor.")

# Função de interface para deletar item
def deletar_itens_gui():
    try:
        selecionado = listbox_itens.curselection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecionar um item para deletar!")
            return
        
        item_id = listbox_itens.get(selecionado[0]).split()[0]
        item_id = int(item_id)

        deletar_item_db(item_id)
        listar_itens_gui()
    except ValueError:
        messagebox.showerror("Erro", "Erro ao tentar deletar o item.")

# Função para listar itens da base de dados
def listar_itens_gui():
    listbox_itens.delete(0, tk.END)
    itens = obter_itens_db()
    for item in itens:
        listbox_itens.insert(tk.END, f"{item[0]} - {item[1]} - Quantidade: {item[2]} - Valor Unitário: R${item[3]:.2f}")

# Função para limpar as entradas
def limpar_entradas():
    entry_item.delete(0, tk.END)
    entry_quantidade.delete(0, tk.END)
    entry_valor.delete(0, tk.END)

# Função para calcular o total
def calcular_totais_gui():
    soma_total = 0
    total_itens = 0
    for item in obter_itens_db():
        total_itens += item[2]
        soma_total += item[2] * item[3]

    desconto = 0
    if total_itens >= 50:
        desconto = 0.15
    elif total_itens >= 20:
        desconto = 0.10
    elif total_itens >= 10:
        desconto = 0.05

    valor_total_com_desconto = soma_total * (1 - desconto)
    result_text.set(f"Valor Total: R${soma_total:.2f}\nDesconto: {desconto * 100:.0f}%\nTotal com Desconto: R${valor_total_com_desconto:.2f}")

# Função para salvar lista
def salvar_lista_gui():
    if not obter_itens_db():
        messagebox.showwarning("Aviso", "Não há itens para salvar!")
        return

    try:
        with open("lista_compras.txt", "w") as file:
            file.write("Lista de Compras:\n")
            for item in obter_itens_db():
                total_item = item[2] * item[3]
                file.write(f"Item: {item[1]}, Quantidade: {item[2]}, Valor: R${item[3]:.2f}, Total: R${total_item:.2f}\n")
            
            file.write("\n")
            file.write(result_text.get())
        
        messagebox.showinfo("Sucesso", "Lista salva com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao salvar o arquivo: {e}")

# Criando a interface gráfica
root = tk.Tk()
root.title("Carrinho de Compras")
root.geometry("650x700")
root.config(bg="#f5f5f5")

criar_banco()

# Frame de entrada de dados
frame_entrada = tk.Frame(root, bg="#f5f5f5")
frame_entrada.pack(pady=20, padx=20, fill="x")

label_item = tk.Label(frame_entrada, text="Nome do item:", bg="#f5f5f5", font=("Arial", 12))
label_item.grid(row=0, column=0, padx=5, sticky="e")

entry_item = tk.Entry(frame_entrada, width=30, font=("Arial", 12))
entry_item.grid(row=0, column=1, padx=5)

label_quantidade = tk.Label(frame_entrada, text="Quantidade:", bg="#f5f5f5", font=("Arial", 12))
label_quantidade.grid(row=1, column=0, padx=5, sticky="e")

entry_quantidade = tk.Entry(frame_entrada, width=30, font=("Arial", 12))
entry_quantidade.grid(row=1, column=1, padx=5)

label_valor = tk.Label(frame_entrada, text="Valor: R$ ", bg="#f5f5f5", font=("Arial", 12))
label_valor.grid(row=2, column=0, padx=5, sticky="e")

entry_valor = tk.Entry(frame_entrada, width=30, font=("Arial", 12))
entry_valor.grid(row=2, column=1, padx=5)

# Botões de ação
button_frame = tk.Frame(root, bg="#f5f5f5")
button_frame.pack(pady=10)

button_adicionar = tk.Button(button_frame, text="Adicionar Item", command=adicionar_itens_gui, width=20, bg="#4CAF50", fg="white", font=("Arial", 12), relief="flat")
button_adicionar.grid(row=0, column=0, padx=10, pady=5)

button_editar = tk.Button(button_frame, text="Editar Item", command=editar_itens_gui, width=20, bg="#FF9800", fg="white", font=("Arial", 12), relief="flat")
button_editar.grid(row=0, column=1, padx=10, pady=5)

button_deletar = tk.Button(button_frame, text="Deletar Item", command=deletar_itens_gui, width=20, bg="#F44336", fg="white", font=("Arial", 12), relief="flat")
button_deletar.grid(row=0, column=2, padx=10, pady=5)

# Lista de itens
listbox_itens = tk.Listbox(root, width=80, height=10, font=("Arial", 12), selectmode=tk.SINGLE)
listbox_itens.pack(pady=10, padx=20)

# Frame de resultados
frame_resultados = tk.Frame(root, bg="#f5f5f5")
frame_resultados.pack(pady=20, padx=20, fill="x")

result_text = tk.StringVar()
label_resultados = tk.Label(frame_resultados, textvariable=result_text, justify=tk.LEFT, bg="#f5f5f5", font=("Arial", 12))
label_resultados.pack()

# Botões de ação
button_calcular = tk.Button(root, text="Calcular Total", command=calcular_totais_gui, width=20, bg="#2196F3", fg="white", font=("Arial", 12), relief="flat")
button_calcular.pack(pady=5)

button_salvar = tk.Button(root, text="Salvar Lista", command=salvar_lista_gui, width=20, bg="#9C27B0", fg="white", font=("Arial", 12), relief="flat")
button_salvar.pack(pady=5)

# Carregar itens na interface ao iniciar
listar_itens_gui()

# Iniciando o loop da interface
root.mainloop()