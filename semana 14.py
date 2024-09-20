import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry


class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")

        # Frame para la lista de eventos
        frame_lista = tk.Frame(self.root)
        frame_lista.pack(pady=10)

        # TreeView para mostrar los eventos
        self.tree = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings", height=10)
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack(side="left")

        # Scrollbar para el TreeView
        scrollbar = ttk.Scrollbar(frame_lista, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        # Frame para la entrada de datos
        frame_entrada = tk.Frame(self.root)
        frame_entrada.pack(pady=10)

        # Campos de entrada
        tk.Label(frame_entrada, text="Fecha").grid(row=0, column=0, padx=5, pady=5)
        self.fecha_entry = DateEntry(frame_entrada, date_pattern='y-mm-dd')
        self.fecha_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_entrada, text="Hora").grid(row=1, column=0, padx=5, pady=5)
        self.hora_entry = tk.Entry(frame_entrada)
        self.hora_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame_entrada, text="Descripción").grid(row=2, column=0, padx=5, pady=5)
        self.desc_entry = tk.Entry(frame_entrada)
        self.desc_entry.grid(row=2, column=1, padx=5, pady=5)

        # Frame para los botones
        frame_botones = tk.Frame(self.root)
        frame_botones.pack(pady=10)

        # Botones
        agregar_btn = tk.Button(frame_botones, text="Agregar Evento", command=self.agregar_evento)
        agregar_btn.grid(row=0, column=0, padx=10)

        eliminar_btn = tk.Button(frame_botones, text="Eliminar Evento Seleccionado", command=self.eliminar_evento)
        eliminar_btn.grid(row=0, column=1, padx=10)

        salir_btn = tk.Button(frame_botones, text="Salir", command=self.root.quit)
        salir_btn.grid(row=0, column=2, padx=10)

    def agregar_evento(self):
        fecha = self.fecha_entry.get()
        hora = self.hora_entry.get()
        descripcion = self.desc_entry.get()

        if fecha and hora and descripcion:
            self.tree.insert('', 'end', values=(fecha, hora, descripcion))
            self.limpiar_entradas()
        else:
            messagebox.showwarning("Entrada incompleta", "Por favor, complete todos los campos")

    def eliminar_evento(self):
        selected_item = self.tree.selection()
        if selected_item:
            confirm = messagebox.askyesno("Confirmar eliminación", "¿Está seguro de eliminar el evento seleccionado?")
            if confirm:
                self.tree.delete(selected_item)
        else:
            messagebox.showwarning("Selección", "Por favor, seleccione un evento para eliminar")

    def limpiar_entradas(self):
        self.fecha_entry.set_date('')
        self.hora_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
