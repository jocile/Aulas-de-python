'''
Este aplicativo é um exemplo de como criar uma interface gráfica para um banco de dados SQLite.
Referência: https://www.youtube.com/watch?v=5qOnzF7RsNA

Algoritmo:
- [X] Adicionar um Label com uma imagem
- [X] Adicionar um Label com um texto
- [X] Adicionar um botão para carregar a segunda tela
- [X] Criar uma função para carregar a segunda tela
- [ ] Conectar ao banco de dados SQLite para acessar os cursos
- [ ] Colocar os resultados na tela

'''

import tkinter as tk
from PIL import ImageTk
import sqlite3
from pathlib import Path
from numpy import random


ROOT_PATH = Path(__file__).parent
bg_color = "silver"
bg_color2 = "#28393a"
bg_color3 = "#3d6466"

def fetch_db():
  connection = sqlite3.connect(ROOT_PATH / "data/cursos.db")
  cursor = connection.cursor()
  # Carrega todas as tabelas do banco de dados
  cursor.execute("SELECT * FROM sqlite_schema WHERE type='table';")
  
  # Armazena todas as tabelas em uma lista
  all_tables = cursor.fetchall()
  
  # Seleciona uma tabela aleatória
  # idx = random.randint(0, len(all_tables[0][1]) - 1)
  # table_name = all_tables[idx][1]
  # cursor.execute(f"SELECT * FROM {all_tables[0][1]} LIMIT 1 OFFSET {idx}")
  
  # Carrega os registros da tabela selecionada
  table_name = all_tables[0][1]
  cursor.execute(f"SELECT * FROM {table_name};")
  table_records = cursor.fetchall()
  
  # Imprime o nome da primeira tabela
  print(all_tables[0][1])
  print(table_records)
  connection.close()

def load_frame1():
    frame1.pack_propagate(False)
    #Logo widget
    logo_img = ImageTk.PhotoImage(file=ROOT_PATH /"../janelas-gui/imgs/Logo_Senac.png")
    logo_widget = tk.Label(frame1, image=logo_img, bg=bg_color)
    logo_widget.image = logo_img
    logo_widget.pack()

    tk.Label(
      frame1,
      text="pronto para seu próximo curso?",
      font=("TKMenuFont", 14),
      bg=bg_color,
      fg="white",
      ).pack()

    # Botão widget
    btn_curso = tk.Button(
      frame1,
      text="Escolher Curso",
      font=("TKHeadingFont", 20),
      bg=bg_color2,
      fg="white",
      cursor="hand2",
      activebackground="#badee2",
      activeforeground="black",
      command=lambda : load_frame2()
      ).pack(pady= 20)
def load_frame2():
    fetch_db()
    #print("Carregando frame2")

# Inicializando o aplicativo
root = tk.Tk()
root.title("Selecionador de cursos")

# Definindo a posição da janela
#root.eval('tk::PlaceWindow . center')
x = root.winfo_screenwidth() // 3
y = int(root.winfo_screenmmheight() * 0.1)
root.geometry('500x600+' + str(x) + '+' + str(y))

# Criando os quadros de widgets
frame1 = tk.Frame(root, width=500, height=600, bg=bg_color)
frame2 = tk.Frame(root, bg=bg_color)
#frame1.grid(row=0, column=0)
#frame2.grid(row=0, column=0)

for frame in (frame1, frame2):
    frame.grid(row=0, column=0)

load_frame1()

# executando o aplicativo
root.mainloop()