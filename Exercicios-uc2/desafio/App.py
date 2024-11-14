'''
 Sistema de Cadastro de Alunos
 Esse sistema deve permitir a inserção, consulta, atualização e exclusão de dados dos alunos.
Fonte: https://jocile.com/Programador/Desafios/cadastro+de+alunos/Desafio+cadastro+de+alunos

Algoritmo:
- [ ] Criar o CRUD
  - [x] Criar a função de cadastro
  - Cadastrar aluno: Permitir a inserção de dados do aluno, incluindo nome, matrícula, curso e data de nascimento.
  - [ ] Criar a função de consulta
  - Consultar aluno: Buscar um aluno por nome ou matrícula e exibir seus dados completos.
  - [ ] Criar a função de atualização
  - Atualizar aluno: Atualizar os dados de um aluno existente, como nome, matrícula, curso ou data de nascimento.
  - [ ] Criar a função de exclusão
  - Excluir aluno: Remover um aluno do sistema por nome ou matrícula.
'''

import sqlite3

from pathlib import Path
ROOT_PATH = Path(__file__).parent

def criar_tabela(conexao, cursor):
	cursor.execute(
	"CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), matricula VARCHAR(20), curso VARCHAR(20), data_nascimento VARCHAR(20))"
	)
	conexao.commit()

def cadastrar_aluno():
    aluno = {}
    aluno['nome'] = input("Digite o nome do aluno: ")
    aluno['matricula'] = input("Digite a matrícula do aluno: ")
    aluno['curso'] = input("Digite o curso do aluno: ")
    aluno['data_nascimento'] = input("Digite a data de nascimento do aluno: ")
    print("Aluno cadastrado com sucesso!")

    conexao = sqlite3.connect(ROOT_PATH / "aluno.db")
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO clientes (nome, matricula, curso, data_nascimento) VALUES (?, ?, ?, ?)", (aluno['nome'], aluno['matricula'], aluno['curso'], aluno['data_nascimento']))
    conexao.commit()
    

def main():
    
    conexao = sqlite3.connect(ROOT_PATH / "aluno.db")
    cursor = conexao.cursor()
    # criar_tabela(conexao, cursor)
    
    while True:
        menu = '''
        -----------------------------------------
        Sistema de Cadastro de Alunos
        -----------------------------------------
        Escolha uma opção:
        0. Criar a tabela
        1. Cadastrar Aluno
        2. Consultar Aluno
        3. Atualizar Aluno
        4. Excluir Aluno
        5. Sair
        '''
        print(menu)
        opcao = input("Digite sua opção: ")

        if opcao == "0":
            criar_tabela(conexao, cursor)
        elif opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            consultar_aluno()
        elif opcao == "3":
            atualizar_aluno()            
        elif opcao == "4":
            excluir_aluno()
        elif opcao == "5":
            print('-' * 30)
            print("Obrigado! Saindo do programa.")
            print('-' * 30)
            break
        else:
            print("Opção inválida!")
    conexao.close()

def consultar_aluno():
    # Implementar a funcionalidade de consulta de aluno
    pass

def atualizar_aluno():
  # Implementar a funcionalidade de atualização de aluno
    pass

def excluir_aluno():
    # Implementar a funcionalidade de exclusão de aluno
    pass

if __name__ == "__main__":
    main()