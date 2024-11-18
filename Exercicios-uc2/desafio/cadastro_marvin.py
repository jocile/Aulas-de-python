'''
Repositório do Marvin:
https://github.com/MarvinTL-24/Marvin-Python/blob/main/desafios/cadastro/cadastro.py
'''

import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
import sqlite3
from pathlib import Path


'''
[]Criar banco de dados.
[]Criar criar as funções principais.
[]Inserir os dados das funções no banco.
[]A função de matricula deve ser a ponte para outra lista no banco de dados.
[]Criar a interface de acordo com as anteriores.
[]Criar um local para visualizar a matricula desejada ja matriculada.
[]Avançar pra editar a matricula na parte principal .
[]Tornar possivel visualizar em tempo real a edição dos dados.
[]Criar item para deletar seguindo os passos anteriores.
[]Criar um visualizador de todos os dados ja cadastrados.
[]Criar um limpador de entradas.
[]Redimensionar a janela e melhorar o estilo de visualização.
[]Melhorar a visualzação dos dados cadastrados, sem afeta o codigo em si.
'''

# Define o caminho para o banco de dados
ROOT_PATH = Path(__file__).parent
db_path = ROOT_PATH / 'data/cadastro_alunos.db'

# Cria o diretório 'data' caso não exista
db_path.parent.mkdir(parents=True, exist_ok=True)

# Classe para gerenciar a conexão e operações no banco de dados
class SistemaCadastroAlunos:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.criar_tabela()

    def criar_tabela(self):
        # Cria as tabelas no banco de dados se não existirem
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS alunos (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                nome TEXT,
                                matricula TEXT UNIQUE,
                                curso TEXT,
                                data_nascimento TEXT)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS notas (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                aluno_id INTEGER,
                                disciplina TEXT,
                                n1 REAL,
                                n2 REAL,
                                n3 REAL,
                                FOREIGN KEY(aluno_id) REFERENCES alunos(id))''')
        self.conn.commit()

    def adicionar_aluno(self, nome, matricula, curso, data_nascimento):
        try:
            # Checa se a matrícula já existe
            self.cursor.execute('SELECT * FROM alunos WHERE matricula = ?', (matricula,))
            if self.cursor.fetchone():
                messagebox.showerror("Erro", "Matrícula já cadastrada.")
                return
            # Insere o novo aluno
            self.cursor.execute('''INSERT INTO alunos (nome, matricula, curso, data_nascimento) 
                                   VALUES (?, ?, ?, ?)''',
                                (nome, matricula, curso, data_nascimento))
            self.conn.commit()
            messagebox.showinfo("Sucesso", "Aluno cadastrado com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao cadastrar aluno: {e}")

    def adicionar_notas_banco(self, matricula, disciplina, n1, n2, n3):
        try:
            # Busca o ID do aluno usando a matrícula
            self.cursor.execute('SELECT id FROM alunos WHERE matricula = ?', (matricula,))
            aluno_id = self.cursor.fetchone()
            if aluno_id:
                aluno_id = aluno_id[0]
                # Insere as notas
                self.cursor.execute('''INSERT INTO notas (aluno_id, disciplina, n1, n2, n3) 
                                       VALUES (?, ?, ?, ?, ?)''', (aluno_id, disciplina, n1, n2, n3))
                self.conn.commit()
                messagebox.showinfo("Sucesso", "Notas adicionadas com sucesso!")
                return True
            else:
                messagebox.showerror("Erro", "Aluno não encontrado!")
                return False
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao adicionar notas: {e}")
            return False
    
    def atualizar_aluno(self, matricula, nome, curso, data_nascimento):
        try:
            self.cursor.execute('''UPDATE alunos SET nome = ?, curso = ?, data_nascimento = ? 
                                   WHERE matricula = ?''', (nome, curso, data_nascimento, matricula))
            self.conn.commit()
            messagebox.showinfo("Sucesso", "Aluno atualizado com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao atualizar aluno: {e}")

    def deletar_aluno(self, matricula):
        try:
            self.cursor.execute('''DELETE FROM notas WHERE aluno_id = (SELECT id FROM alunos WHERE matricula = ?)''', (matricula,))
            self.cursor.execute('''DELETE FROM alunos WHERE matricula = ?''', (matricula,))
            self.conn.commit()
            messagebox.showinfo("Sucesso", "Aluno e suas notas deletados com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao deletar aluno: {e}")

    def buscar_notas_por_matricula(self, matricula):
        try:
            self.cursor.execute('''SELECT disciplina, n1, n2, n3 
                                   FROM notas 
                                   JOIN alunos ON notas.aluno_id = alunos.id 
                                   WHERE alunos.matricula = ?''', (matricula,))
            return self.cursor.fetchall()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao buscar notas: {e}")
            return []
    
    def buscar_todos_alunos(self):
        try:
            self.cursor.execute('''SELECT matricula, nome, curso, data_nascimento FROM alunos''')
            return self.cursor.fetchall()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao buscar alunos: {e}")
            return []

    def buscar_aluno_por_matricula(self, matricula):
        self.cursor.execute('SELECT * FROM alunos WHERE matricula = ?', (matricula,))
        return self.cursor.fetchone()


# Aplicação Tkinter
class Aplicacao:
    def __init__(self, root):
        self.sistema = SistemaCadastroAlunos(db_path)
        self.root = root
        self.root.title("Sistema de Cadastro de Alunos")
        self.create_widgets()
        self.root.geometry("400x700")
        self.root.resizable(False, False)

    def create_widgets(self):
        frame = ttk.Frame(self.root, padding="10")
        frame.grid(row=0, column=0, sticky="nsew")

        # Seção de cadastro de alunos
        ttk.Label(frame, text="Cadastro de Aluno", font=("Arial", 12, "bold")).grid(row=0, columnspan=2, pady=10)

        ttk.Label(frame, text="Nome:").grid(row=1, column=0, sticky="w", pady=2)
        self.nome_entry = ttk.Entry(frame)
        self.nome_entry.grid(row=1, column=1, sticky="ew", pady=2)

        ttk.Label(frame, text="Matrícula:").grid(row=2, column=0, sticky="w", pady=2)
        self.matricula_entry = ttk.Entry(frame)
        self.matricula_entry.grid(row=2, column=1, sticky="ew", pady=2)

        ttk.Label(frame, text="Curso:").grid(row=3, column=0, sticky="w", pady=2)
        self.curso_entry = ttk.Combobox(frame, values=["Programação", "Designer"])
        self.curso_entry.grid(row=3, column=1, sticky="ew", pady=2)

        ttk.Label(frame, text="Data de Nascimento (DD/MM/YYYY):").grid(row=4, column=0, sticky="w", pady=2)
        self.nascimento_entry = ttk.Entry(frame)
        self.nascimento_entry.grid(row=4, column=1, sticky="ew", pady=2)

        ttk.Button(frame, text="Cadastrar Aluno", command=self.cadastrar_aluno).grid(row=5, columnspan=2, pady=10, sticky="ew")

        # Seção de adicionar notas
        ttk.Label(frame, text="Adicionar Notas", font=("Arial", 12, "bold")).grid(row=6, columnspan=2, pady=10)

        ttk.Label(frame, text="Disciplina:").grid(row=7, column=0, sticky="w", pady=2)
        self.disciplina_entry = ttk.Entry(frame)
        self.disciplina_entry.grid(row=7, column=1, sticky="ew", pady=2)

        ttk.Label(frame, text="Nota N1:").grid(row=8, column=0, sticky="w", pady=2)
        self.n1_entry = ttk.Entry(frame)
        self.n1_entry.grid(row=8, column=1, sticky="ew", pady=2)

        ttk.Label(frame, text="Nota N2:").grid(row=9, column=0, sticky="w", pady=2)
        self.n2_entry = ttk.Entry(frame)
        self.n2_entry.grid(row=9, column=1, sticky="ew", pady=2)

        ttk.Label(frame, text="Nota N3:").grid(row=10, column=0, sticky="w", pady=2)
        self.n3_entry = ttk.Entry(frame)
        self.n3_entry.grid(row=10, column=1, sticky="ew", pady=2)

        ttk.Button(frame, text="Adicionar Notas", command=self.adicionar_notas).grid(row=11, columnspan=2, pady=10, sticky="ew")
        ttk.Button(frame, text="Exibir Notas", command=self.exibir_notas).grid(row=12, columnspan=2, pady=10, sticky="ew")
        
        # Seção de atualizar ou deletar aluno
        ttk.Label(frame, text="Atualizar ou Deletar Aluno", font=("Arial", 12, "bold")).grid(row=13, columnspan=2, pady=10)

        # Entradas de atualização e exclusão
        ttk.Label(frame, text="Matrícula para buscar aluno:").grid(row=14, column=0, sticky="w", pady=2)
        self.matricula_atualizar_entry = ttk.Entry(frame)
        self.matricula_atualizar_entry.grid(row=14, column=1, sticky="ew", pady=2)

        ttk.Button(frame, text="Buscar Aluno", command=self.buscar_aluno).grid(row=15, columnspan=2, pady=5, sticky="ew")

        # Exibir campos de dados do aluno
        self.dados_aluno_label = ttk.Label(frame, text="", font=("Arial", 10), foreground="blue")
        self.dados_aluno_label.grid(row=16, columnspan=2, pady=5, sticky="w")

        self.atualizar_button = ttk.Button(frame, text="Atualizar Aluno", command=self.atualizar_aluno)
        self.atualizar_button.grid(row=17, columnspan=2, pady=5, sticky="ew")
        self.deletar_button = ttk.Button(frame, text="Deletar Aluno", command=self.deletar_aluno)
        self.deletar_button.grid(row=18, columnspan=2, pady=5, sticky="ew")

        # Botão para exibir todos os alunos
        ttk.Button(frame, text="Exibir Todos os Alunos", command=self.exibir_todos_alunos).grid(row=19, columnspan=2, pady=5, sticky="ew")

    def cadastrar_aluno(self):
        nome = self.nome_entry.get()
        matricula = self.matricula_entry.get()
        curso = self.curso_entry.get()
        data_nascimento = self.nascimento_entry.get()

        self.sistema.adicionar_aluno(nome, matricula, curso, data_nascimento)

    def adicionar_notas(self):
        matricula = self.matricula_entry.get()
        disciplina = self.disciplina_entry.get()
        try:
            n1 = float(self.n1_entry.get())
            n2 = float(self.n2_entry.get())
            n3 = float(self.n3_entry.get())
            self.sistema.adicionar_notas_banco(matricula, disciplina, n1, n2, n3)
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira notas válidas!")

    def exibir_notas(self):
        matricula = self.matricula_entry.get()
        notas = self.sistema.buscar_notas_por_matricula(matricula)
        resultado = "\n".join([f"Disciplina: {disc}, N1: {n1}, N2: {n2}, N3: {n3}" for disc, n1, n2, n3 in notas])
        messagebox.showinfo("Notas", resultado if resultado else "Nenhuma nota encontrada.")
    
    def exibir_todos_alunos(self):
        alunos = self.sistema.buscar_todos_alunos()
        if alunos:
            resultado = "\n".join([f"Matricula: {matricula}, Nome: {nome}, Curso: {curso}, Data Nascimento: {data_nascimento}" 
                                   for matricula, nome, curso, data_nascimento in alunos])
            messagebox.showinfo("Todos os Alunos", resultado)
        else:
            messagebox.showinfo("Todos os Alunos", "Nenhum aluno cadastrado.")

    def buscar_aluno(self):
        matricula = self.matricula_atualizar_entry.get()
        aluno = self.sistema.buscar_aluno_por_matricula(matricula)
        
        if aluno:
            nome, matricula, curso, data_nascimento = aluno[1], aluno[2], aluno[3], aluno[4]
            # Exibir dados do aluno
            self.dados_aluno_label.config(text=f"Nome: {nome}\nCurso: {curso}\nData Nascimento: {data_nascimento}")
            
            # Habilitar botões de atualização e exclusão
            self.atualizar_button.config(state="normal")
            self.deletar_button.config(state="normal")
        else:
            self.dados_aluno_label.config(text="Aluno não encontrado.")
            self.atualizar_button.config(state="disabled")
            self.deletar_button.config(state="disabled")

    def atualizar_aluno(self):
        matricula = self.matricula_atualizar_entry.get()
        nome = self.nome_entry.get()
        curso = self.curso_entry.get()
        data_nascimento = self.nascimento_entry.get()

        if not matricula:
            messagebox.showerror("Erro", "Por favor, insira a matrícula do aluno.")
            return

        aluno = self.sistema.buscar_aluno_por_matricula(matricula)
        if aluno:
            self.sistema.atualizar_aluno(matricula, nome, curso, data_nascimento)
        else:
            messagebox.showerror("Erro", "Aluno não encontrado para atualização.")

    def deletar_aluno(self):
        matricula = self.matricula_atualizar_entry.get()

        if not matricula:
            messagebox.showerror("Erro", "Por favor, insira a matrícula do aluno.")
            return

        aluno = self.sistema.buscar_aluno_por_matricula(matricula)
        if aluno:
            confirmacao = messagebox.askyesno("Confirmação", "Tem certeza que deseja deletar este aluno?")
            if confirmacao:
                self.sistema.deletar_aluno(matricula)
                self.dados_aluno_label.config(text="")
                self.atualizar_button.config(state="disabled")
                self.deletar_button.config(state="disabled")
        else:
            messagebox.showerror("Erro", "Aluno não encontrado para exclusão.")

# Inicia a aplicação
if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacao(root)
    root.mainloop()