import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

# Cria uma conexão com o banco de dados
conexao = sqlite3.connect(ROOT_PATH / 'data/banco_de_dados.db')

# Cria um cursor para executar comandos SQL
cursor = conexao.cursor()

# Cria a tabela de clientes
def criar_tabela_clientes(): 
  cursor.execute(
    """CREATE TABLE clientes (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          nome VARCHAR(100),
          email VARCHAR(150)
        )
    """
    )
  conexao.commit()

# Insere dados na tabela de clientes
def inserir_clientes():
  cursor.execute(
    """INSERT INTO clientes (nome, email) VALUES
          ('João', 'joao@email.com'),
          ('Maria', 'maria@email.com'),
          ('José', 'jose@email.com')
    """
  )
  conexao.commit()

# Mostra todos os clientes
def mostrar_clientes():
  cursor.execute("SELECT * FROM clientes")
  for linha in cursor.fetchall():
    print(f"ID: {linha[0]}, Nome: {linha[1]}, Email: {linha[2]}")

criar_tabela_clientes()
# inserir_clientes()
# mostrar_clientes()

# Fecha a conexão com o banco de dados
conexao.close()