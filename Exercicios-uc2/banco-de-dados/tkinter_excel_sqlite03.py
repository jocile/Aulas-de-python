'''
Inserindo dados dados na planilha do Excel
referência: https://www.youtube.com/watch?v=8m4uDS_nyCk

Algoritmo:
- [x] Carregar dados de uma planilha
- [x] Exibir os dados em uma janela Tkinter
- [x] Inserir novos registros na planilha
- [ ] Organizar o código criando funções separadas para:
  - [x] Criar uma função para carregar a janela Tkinter
  - [x] Criar widgets de entrada
  - [x] Configurar o TreeView
  - [ ] Configurar os botões
  - [ ] Configurar os eventos
- [ ] Salvar os dados em um banco de dados Sqlite

'''

import tkinter as tk
from tkinter import ttk
from pathlib import Path
import openpyxl

ROOT_PATH = Path(__file__).parent
path = ROOT_PATH / "data/people.xlsx"

def load_data():
    workbook = openpyxl.load_workbook(path)
    sheet = workbook.active

    list_values = list(sheet.values)
    print(list_values)
    for col_name in list_values[0]:
        treeview.heading(col_name, text=col_name)

    for value_tuple in list_values[1:]:
        treeview.insert('', tk.END, values=value_tuple)

def insert_row():
    name = name_entry.get()
    age = int(age_spinbox.get())
    subscription_status = status_combobox.get()
    employment_status = "Employed" if a.get() else "Unemployed"

    print(name, age, subscription_status, employment_status)

    # Insert row into Excel sheet
    workbook = openpyxl.load_workbook(path)
    sheet = workbook.active
    row_values = [name, age, subscription_status, employment_status]
    sheet.append(row_values)
    workbook.save(path)

    # Insert row into treeview
    treeview.insert('', tk.END, values=row_values)
    
    # Clear the values
    name_entry.delete(0, "end")
    name_entry.insert(0, "Name")
    age_spinbox.delete(0, "end")
    age_spinbox.insert(0, "Age")
    status_combobox.set(combo_list[0])
    checkbutton.state(["!selected"])

def toggle_mode():
    if mode_switch.instate(["selected"]):
        print("Selecionado")
    else:
        print("Desmarcado")

def criar_frame(root):
    frame = ttk.Frame(root)
    frame.pack()
    
    # Frame para widgets
    widgets_frame = ttk.LabelFrame(frame, text="Insert Row")
    widgets_frame.grid(row=0, column=0, padx=20, pady=10)
    
    # Frame para TreeView
    treeFrame = ttk.Frame(frame)
    treeFrame.grid(row=0, column=1, pady=10)
    
    return frame, widgets_frame, treeFrame

def criar_widgets_entrada(widgets_frame):
    name_entry = ttk.Entry(widgets_frame)
    name_entry.insert(0, "Name")
    name_entry.bind("<FocusIn>", lambda e: name_entry.delete('0', 'end'))
    name_entry.grid(row=0, column=0, padx=5, pady=(0, 5), sticky="ew")

    age_spinbox = ttk.Spinbox(widgets_frame, from_=18, to=100)
    age_spinbox.insert(0, "Age")
    age_spinbox.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

    status_combobox = ttk.Combobox(widgets_frame, values=combo_list)
    status_combobox.current(0)
    status_combobox.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

    a = tk.BooleanVar()
    checkbutton = ttk.Checkbutton(widgets_frame, text="Employed", variable=a)
    checkbutton.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")
    
    return name_entry, age_spinbox, status_combobox, checkbutton, a

def configurar_treeview(treeFrame):
    treeScroll = ttk.Scrollbar(treeFrame)
    treeScroll.pack(side="right", fill="y")

    cols = ("Name", "Age", "Subscription", "Employment")
    treeview = ttk.Treeview(treeFrame, show="headings",
                           yscrollcommand=treeScroll.set, columns=cols, height=13)
    
    treeview.column("Name", width=100)
    treeview.column("Age", width=50)
    treeview.column("Subscription", width=100)
    treeview.column("Employment", width=100)
    treeview.pack()
    
    treeScroll.config(command=treeview.yview)
    return treeview

root = tk.Tk()
combo_list = ["Subscribed", "Not Subscribed", "Other"]
frame, widgets_frame, treeFrame = criar_frame(root)
name_entry, age_spinbox, status_combobox, checkbutton, a = criar_widgets_entrada(widgets_frame)
treeview = configurar_treeview(treeFrame)

button = ttk.Button(widgets_frame, text="Insert", command=insert_row)
button.grid(row=4, column=0, padx=5, pady=5, sticky="nsew")

separator = ttk.Separator(widgets_frame)
separator.grid(row=5, column=0, padx=(20, 10), pady=10, sticky="ew")

mode_switch = ttk.Checkbutton(
    widgets_frame, text="Mode", command=toggle_mode)
mode_switch.grid(row=6, column=0, padx=5, pady=10, sticky="nsew")

load_data()

root.mainloop()