import tkinter as tk
from tkinter import messagebox, filedialog
import os
from datetime import datetime
from pathlib import Path

ROOT_PATH = Path(__file__).parent
# Função para exibir a lista de compras
def exibir_lista():
    # Limpar a área de exibição
    lista_texto.delete(1.0, tk.END)

    if not compras:
        lista_texto.insert(tk.END, "Nenhum produto na lista.\n")
        return

    total = 0
    lista = ""
    for produto, valor in compras:
        lista += f"{produto}: R$ {valor:.2f}\n"
        total += valor

    lista += f"\nValor Total: R$ {total:.2f}"
    lista_texto.insert(tk.END, lista)

# Função para adicionar um produto à lista
def adicionar_produto():
    produto = input_produto.get()
    valor = input_valor.get()
    
    if produto and valor:
        try:
            valor = float(valor)  # Garantir que o valor seja um número
            compras.append([produto, valor])
            input_produto.delete(0, tk.END)  # Limpar o campo de entrada
            input_valor.delete(0, tk.END)  # Limpar o campo de entrada
            exibir_lista()
        except ValueError:
            messagebox.showerror("Erro", "Valor inválido! Digite um número válido para o valor.")
    else:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos.")

# Função para excluir um produto
def excluir_produto():
    produto_excluir = input_produto.get()
    for item in compras:
        if item[0].lower() == produto_excluir.lower():
            compras.remove(item)
            input_produto.delete(0, tk.END)
            exibir_lista()
            return
    messagebox.showerror("Erro", f"Produto '{produto_excluir}' não encontrado.")

# Função para imprimir a lista (exibir em uma nova janela)
def imprimir_lista():
    if not compras:
        messagebox.showinfo("Lista Vazia", "Não há produtos na lista para imprimir.")
        return
    
    # Criando nova janela para exibir a lista
    imprimir_window = tk.Toplevel(root)
    imprimir_window.title("Imprimir Lista de Compras")
    
    # Exibir a lista na nova janela
    lista_texto_imprimir = tk.Text(imprimir_window, height=20, width=50, font=("Helvetica", 12), wrap="word", bd=2, relief="sunken")
    lista_texto_imprimir.pack(padx=20, pady=20)
    
    total = 0
    lista = ""
    for produto, valor in compras:
        lista += f"{produto}: R$ {valor:.2f}\n"
        total += valor

    lista += f"\nValor Total: R$ {total:.2f}"
    lista_texto_imprimir.insert(tk.END, lista)

# Função para salvar a lista de compras em uma pasta específica
def salvar_lista():
    if not compras:
        messagebox.showinfo("Lista Vazia", "Não há produtos na lista para salvar.")
        return
    
    # Defina o diretório específico onde as listas serão salvas (modifique conforme necessário)
    pasta_destino = ROOT_PATH  # Escolha o caminho da pasta
    
    # Se a pasta não existir, crie-a
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)
    
    # Criar o nome do arquivo com base na data e hora
    nome_arquivo = datetime.now().strftime("lista_compras_%Y_%m_%d_%H_%M.txt")
    caminho_arquivo = os.path.join(pasta_destino, nome_arquivo)

    try:
        with open(caminho_arquivo, "w", encoding="utf-8") as arquivo_salvo:
            total = 0
            for produto, valor in compras:
                arquivo_salvo.write(f"{produto}: R$ {valor:.2f}\n")
                total += valor
            arquivo_salvo.write(f"\nValor Total: R$ {total:.2f}")
        messagebox.showinfo("Sucesso", f"Lista de compras salva em: {caminho_arquivo}")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao salvar a lista: {e}")


# Função para recuperar a lista de compras a partir de um arquivo
def recuperar_lista():
    pasta_destino = ROOT_PATH  # Diretório onde os arquivos de lista são salvos

    # Abrir a janela de seleção de arquivo para o usuário escolher qual lista recuperar
    arquivo = filedialog.askopenfilename(
        title="Selecione um arquivo de lista de compras",
        filetypes=[("Arquivos de texto", "*.txt")],
        initialdir=pasta_destino  # Apontar para a pasta de destino onde as listas são armazenadas
    )
    
    if not arquivo:
        return  # Se o usuário cancelar, não faz nada
    
    try:
        with open(arquivo, "r") as f:
            linhas = f.readlines()
            compras.clear()  # Limpar a lista atual antes de carregar a nova
            
            produto = None
            valor = None
            for linha in linhas:
                linha = linha.strip()
                if linha.startswith("Valor Total:"):
                    continue  # Ignorar linha com o valor total
                elif linha and ": R$" in linha:
                    produto, valor = linha.split(": R$")
                    valor = float(valor.replace(",", "."))
                    compras.append([produto.strip(), valor])
            
            # Exibir a lista após recuperação
            exibir_lista()
            messagebox.showinfo("Sucesso", f"Lista de compras recuperada de {arquivo} com sucesso!")
    
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao recuperar a lista: {e}")

# Função para começar uma nova lista de compras (limpar a lista atual)
def comecar_nova_lista():
    if compras:
        resposta = messagebox.askyesno("Confirmar", "Você tem certeza que deseja começar uma nova lista? A lista atual será apagada.")
        if resposta:
            compras.clear()  # Limpar a lista atual
            exibir_lista()  # Atualizar a exibição
            messagebox.showinfo("Nova Lista", "Uma nova lista de compras foi iniciada.")
    else:
        messagebox.showinfo("Nova Lista", "A lista de compras já está vazia. Comece a adicionar produtos.")

# Função para sair do aplicativo
def sair():
    root.quit()

# Lista de compras (inicialmente vazia)
compras = []

# Criar a janela principal
root = tk.Tk()
root.title("Lista de Compras")

# Definir o tamanho da janela
root.geometry("600x700")
root.config(bg="#f0f0f0")

# Criar o menu
menu = tk.Menu(root)
root.config(menu=menu)

# Criar opções do menu
menu_compras = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Compras", menu=menu_compras)
menu_compras.add_command(label="Adicionar Produto", command=adicionar_produto)
menu_compras.add_command(label="Excluir Produto", command=excluir_produto)
menu_compras.add_command(label="Exibir Lista", command=exibir_lista)
menu_compras.add_command(label="Imprimir Lista", command=imprimir_lista)
menu_compras.add_command(label="Salvar Lista", command=salvar_lista)
menu_compras.add_command(label="Recuperar Lista", command=recuperar_lista)
menu_compras.add_command(label="Começar Nova Lista", command=comecar_nova_lista)  # Novo comando para começar nova lista
menu_compras.add_separator()
menu_compras.add_command(label="Sair", command=sair)

# Adicionar widgets para interação do usuário com mais estilo
label_produto = tk.Label(root, text="Produto:", font=("Helvetica", 12), bg="#f0f0f0")
label_produto.pack(pady=5)

input_produto = tk.Entry(root, font=("Helvetica", 12), width=30, borderwidth=2, relief="solid")
input_produto.pack(pady=5)

label_valor = tk.Label(root, text="Valor:", font=("Helvetica", 12), bg="#f0f0f0")
label_valor.pack(pady=5)

input_valor = tk.Entry(root, font=("Helvetica", 12), width=30, borderwidth=2, relief="solid")
input_valor.pack(pady=5)

# Botões de adicionar e excluir com estilo
botao_adicionar = tk.Button(root, text="Adicionar Produto", font=("Helvetica", 12), bg="#4CAF50", fg="white", command=adicionar_produto, relief="raised", width=20)
botao_adicionar.pack(pady=10)

botao_excluir = tk.Button(root, text="Excluir Produto", font=("Helvetica", 12), bg="#f44336", fg="white", command=excluir_produto, relief="raised", width=20)
botao_excluir.pack(pady=10)

botao_salvar = tk.Button(root, text="Salvar", font=("Helvetica", 12), bg="#FFC107", fg="white", command=salvar_lista, relief="raised", width=20)
botao_salvar.pack(pady=10)

botao_nova_lista = tk.Button(root, text="Nova lista", font=("Helvetica", 12), bg="#333333", fg="white", command=comecar_nova_lista, relief="raised", width=20)
botao_nova_lista.pack(pady=10)

# Área de texto para exibir a lista de compras, com borda e scroll
lista_texto = tk.Text(root, height=10, width=40, font=("Helvetica", 12), wrap="word", bd=2, relief="sunken")
lista_texto.pack(pady=10)

# Botão de imprimir a lista 
botao_imprimir = tk.Button(root, text="Imprimir Lista", font=("Helvetica", 12), bg="#2196F3", fg="white", command=imprimir_lista, relief="raised", width=20)
botao_imprimir.pack(pady=10)

# Botão de Recuperar uma a lista antiga
botao_recuperar = tk.Button(root, text="Recuperar uma Lista anterior", font=("Helvetica", 12), bg="#2196F3", fg="white", command=recuperar_lista, relief="raised", width=30)
botao_recuperar.pack(pady=10)

# Iniciar a interface gráfica
root.mainloop()