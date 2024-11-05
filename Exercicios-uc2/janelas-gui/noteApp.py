import tkinter as tk

class NoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicação de Notas")
        self.root.geometry("400x300")

        # Entrada de texto
        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=10)

        # Botão para adicionar nota
        self.add_button = tk.Button(root, text="Adicionar Nota", command=self.add_note)
        self.add_button.pack(pady=5)

        # Área de texto para listar notas
        self.text_area = tk.Text(root, width=50, height=10)
        self.text_area.pack(pady=10)

    def add_note(self):
        note = self.entry.get()
        self.text_area.insert(tk.END, note + "\n")
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = NoteApp(root)
    root.mainloop()