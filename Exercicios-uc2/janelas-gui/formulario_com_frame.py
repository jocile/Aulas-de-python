'''
Formulário com tkinter seguindo o exemplo em: https://jocile.com/Programador/Python/Interface+grafica/Formulario-de-Entrada-de-Dados-com-Tkinter
'''

import tkinter as tk
from tkinter import ttk

def enviar_dados():
  # Innformações do usuário
  firstname = first_name_entry.get()
  idade = age_spinbox.get()
  print(f"Nome: {firstname}, Idade: {idade}")

# Criar a janela principal
window = tk.Tk()
window.title("Cadastro de Usuário")

# Criar um frame para conter os widgets do formulário
frame = tk.Frame(window)
frame.pack()

# Criar os widgets do formulário
user_info_frame = tk.LabelFrame(frame, text="Informações do Usuário")
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

first_name_label = tk.Label(user_info_frame, text="Primeiro nome:")
first_name_label.grid(row=0, column=0)
last_name_label = tk.Label(user_info_frame, text="Último nome:")
last_name_label.grid(row=0, column=1)

first_name_entry = tk.Entry(user_info_frame)
last_name_entry = tk.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

title_label = tk.Label(user_info_frame, text="Título:")
title_combobox = ttk.Combobox(user_info_frame, values=["", "Sr.", "Sra.", "Dr.", "Dra."])
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)

age_label = tk.Label(user_info_frame, text="Idade:")
age_spinbox = tk.Spinbox(user_info_frame, from_=18, to=100)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

nationality_label = tk.Label(user_info_frame, text="Nacionalidade:")
nationality_combobox = ttk.Combobox(user_info_frame, values=["", "Brasileiro", "Argentino", "Chileno", "Colombiano", "Espanhol", "Francês", "Inglês", "Italiano", "Português", "Russo", "Sueco", "Turco"])
nationality_label.grid(row=2, column=1)
nationality_combobox.grid(row=3, column=1)

for Widget in user_info_frame.winfo_children():
    Widget.grid_configure(padx=10, pady=5)

# Informações do curso
course_frame = tk.LabelFrame(frame, text="Informações do Curso")
course_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

registered_label = tk.Label(course_frame, text="Estatus do Curso:")
registered_check = tk.Checkbutton(course_frame, text="Matrícula registrada")
registered_label.grid(row=0, column=0)
registered_check.grid(row=1, column=0)

numcourses_label = tk.Label(course_frame, text="# Cursos concluídos:")
numcourses_spinbox = tk.Spinbox(course_frame, from_=0, to='infinity')
numcourses_label.grid(row=0, column=1)
numcourses_spinbox.grid(row=1, column=1)

numsemesters_label = tk.Label(course_frame, text="# Semestres:")
numsemesters_spinbox = tk.Spinbox(course_frame, from_=0, to='infinity')
numsemesters_label.grid(row=0, column=2)
numsemesters_spinbox.grid(row=1, column=2)

for Widget in course_frame.winfo_children():
    Widget.grid_configure(padx=10, pady=5)

# Aceitando os termos
terms_frame = tk.LabelFrame(frame, text="Termos e Condições")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

terms_check = tk.Checkbutton(terms_frame, text="Eu aceito os termos e condições")
terms_check.grid(row=0, column=0)

# Botão de envio
submit_button = tk.Button(frame, text="Enviar dados", command=enviar_dados)
submit_button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

window.mainloop()