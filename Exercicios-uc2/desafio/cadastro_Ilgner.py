'''
Repositório do Ilgner:
https://github.com/IllgnerPeixoto/Aula_py/blob/main/Desafios.py/Cadastro_Aluno_Janela_CRUD.py
'''

import tkinter as tk
from tkinter import messagebox
import os
from datetime import datetime
from pathlib import Path

ROOT_PATH = Path(__file__).parent

class CadastroAlunosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Alunos")
        self.root.geometry("600x600")  # Ajustei a altura para acomodar mais campos

        self.alunos = []  # Lista para armazenar os dados dos alunos

        # Labels e campos de entrada com grid
        self.nome_label = tk.Label(root, text="Nome:")
        self.nome_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")

        self.nome_entry = tk.Entry(root)
        self.nome_entry.grid(row=0, column=1, padx=10, pady=5)

        self.idade_label = tk.Label(root, text="Idade:")
        self.idade_label.grid(row=0, column=2, padx=10, pady=5, sticky="e")

        self.idade_entry = tk.Entry(root)
        self.idade_entry.grid(row=0, column=3, padx=10, pady=5)

        self.curso_label = tk.Label(root, text="Curso:")
        self.curso_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")

        self.curso_entry = tk.Entry(root)
        self.curso_entry.grid(row=1, column=1, padx=10, pady=5)

        self.matricula_label = tk.Label(root, text="Matrícula:")
        self.matricula_label.grid(row=1, column=2, padx=10, pady=5, sticky="e")

        self.matricula_entry = tk.Entry(root)
        self.matricula_entry.grid(row=1, column=3, padx=10, pady=5)

        # Botões para operações CRUD
        self.criar_btn = tk.Button(root, text="Cadastrar", command=self.cadastrar)
        self.criar_btn.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

        self.atualizar_btn = tk.Button(root, text="Atualizar", command=self.atualizar)
        self.atualizar_btn.grid(row=6, column=1, columnspan=2, padx=10, pady=5)

        self.deletar_btn = tk.Button(root, text="Deletar", command=self.deletar)
        self.deletar_btn.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

        self.listar_btn = tk.Button(root, text="Listar Alunos", command=self.listar)
        self.listar_btn.grid(row=7, column=1, columnspan=2, padx=10, pady=5)
        
        self.salvar_btn = tk.Button(root, text="Salvar", command=self.salvar_lista)
        self.salvar_btn.grid(row=8, column=1, columnspan=2, padx=10, pady=5)

        # Listbox para mostrar os alunos cadastrados
        self.listbox = tk.Listbox(root, width=40, height=10)
        self.listbox.grid(row=2, column=1, columnspan=2, padx=10, pady=10)

    def cadastrar(self):
        nome = self.nome_entry.get()
        idade = self.idade_entry.get()
        curso = self.curso_entry.get()
        matricula = self.matricula_entry.get()

        if not nome or not idade or not curso or not matricula:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
            return

        aluno = {"nome": nome, "idade": idade, "curso": curso, "matricula": matricula}
        self.alunos.append(aluno)

        messagebox.showinfo("Sucesso", "Aluno cadastrado com sucesso!")
        self.nome_entry.delete(0, tk.END)
        self.idade_entry.delete(0, tk.END)
        self.curso_entry.delete(0, tk.END)
        self.matricula_entry.delete(0, tk.END)
        self.listar()

    def listar(self):
        self.listbox.delete(0, tk.END)  # Limpa a listbox antes de adicionar os alunos
        for aluno in self.alunos:
            self.listbox.insert(tk.END, f"Nome: {aluno['nome']}, Idade: {aluno['idade']}, Curso: {aluno['curso']}, Matrícula: {aluno['matricula']}")

    def atualizar(self):
        selected_index = self.listbox.curselection()
        if not selected_index:
            messagebox.showerror("Erro", "Selecione um aluno para atualizar!")
            return

        index = selected_index[0]
        nome = self.nome_entry.get()
        idade = self.idade_entry.get()
        curso = self.curso_entry.get()
        matricula = self.matricula_entry.get()

        if not nome or not idade or not curso or not matricula:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
            return

        self.alunos[index] = {"nome": nome, "idade": idade, "curso": curso, "matricula": matricula}

        messagebox.showinfo("Sucesso", "Aluno atualizado com sucesso!")
        self.nome_entry.delete(0, tk.END)
        self.idade_entry.delete(0, tk.END)
        self.curso_entry.delete(0, tk.END)
        self.matricula_entry.delete(0, tk.END)
        self.listar()

    def deletar(self):
        selected_index = self.listbox.curselection()
        if not selected_index:
            messagebox.showerror("Erro", "Selecione um aluno para deletar!")
            return

        index = selected_index[0]
        del self.alunos[index]

        messagebox.showinfo("Sucesso", "Aluno deletado com sucesso!")
        self.listar()
    
    def salvar_lista(self):
        if not self.alunos:
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
                for produto, valor in self.alunos:
                    # FIXME: Too many values to unpack (expected 2)
                    arquivo_salvo.write(f"{produto}: R$ {valor:.2f}\n")
                    total += valor
                arquivo_salvo.write(f"\nValor Total: R$ {total:.2f}")
            messagebox.showinfo("Sucesso", f"Lista de compras salva em: {caminho_arquivo}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar a lista: {e}")    

           

# Configuração da interface principal
root = tk.Tk()
app = CadastroAlunosApp(root)
root.mainloop()