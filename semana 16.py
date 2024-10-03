import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")
        self.root.geometry("400x400")

        # Campo de entrada para nuevas tareas
        self.entry = tk.Entry(root, width=30)
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.add_task)  # Atajo para añadir tarea

        # Lista de tareas
        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, height=10, width=50)
        self.task_listbox.pack(pady=10)

        # Botones
        self.add_button = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(pady=5)

        self.complete_button = tk.Button(root, text="Marcar como Completada", command=self.complete_task)
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(pady=5)

        # Bind de atajos de teclado
        self.root.bind("<c>", self.complete_task)  # Atajo para completar tarea
        self.root.bind("<d>", self.delete_task)  # Atajo para eliminar tarea
        self.root.bind("<Escape>", lambda event: root.quit())  # Atajo para salir

        # Tareas
        self.tasks = []

    def add_task(self, event=None):
        task = self.entry.get()
        if task != "":
            self.task_listbox.insert(tk.END, task)
            self.tasks.append({"task": task, "completed": False})
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Entrada Vacía", "Escribe una tarea antes de añadirla.")

    def complete_task(self, event=None):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.tasks[selected_task_index]["completed"] = True
            self.task_listbox.itemconfig(selected_task_index, {'fg': 'green'})
        except IndexError:
            messagebox.showwarning("Selecciona una Tarea", "Selecciona una tarea para marcar como completada.")

    def delete_task(self, event=None):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_task_index)
            del self.tasks[selected_task_index]
        except IndexError:
            messagebox.showwarning("Selecciona una Tarea", "Selecciona una tarea para eliminarla.")


# Inicializar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
