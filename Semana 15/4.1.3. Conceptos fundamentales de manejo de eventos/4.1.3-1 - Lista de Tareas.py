import tkinter as tk
from tkinter import messagebox, ttk


# Clase que representa la aplicación de Lista de Tareas
class TaskApp:
    def __init__(self, root):
        """Constructor de la clase TaskApp, inicializa la interfaz gráfica y sus componentes."""
        self.root = root
        self.root.title("Lista de Tareas")
        self.root.geometry("500x500")

        # Configuración de estilos para el TreeView
        self.style = ttk.Style()
        self.style.configure("Treeview", rowheight=25)

        # Campo de entrada para nueva tarea
        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.pack(pady=10)

        # Botón para añadir tarea
        self.add_button = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(pady=5)

        # Lista de tareas (TreeView) para mostrar las tareas ingresadas
        self.tasks = ttk.Treeview(root, columns=('Tarea'), show='headings', selectmode='browse')
        self.tasks.heading('Tarea', text='Descripción')
        self.tasks.pack(fill=tk.BOTH, expand=True, pady=10)

        # Configurar evento de doble clic para marcar/desmarcar como completada
        self.tasks.bind('<Double-1>', self.toggle_task_completion)

        # Contenedor para los botones de acciones
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        # Botón para marcar una tarea como completada
        self.complete_button = tk.Button(button_frame, text="Marcar como Completada",
                                         command=self.mark_task)
        self.complete_button.grid(row=0, column=0, padx=5)

        # Botón para desmarcar una tarea
        self.uncomplete_button = tk.Button(button_frame, text="Desmarcar Tarea",
                                           command=self.unmark_task)
        self.uncomplete_button.grid(row=0, column=1, padx=5)

        # Botón para eliminar una tarea seleccionada
        self.delete_button = tk.Button(button_frame, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.grid(row=0, column=2, padx=5)

        # Configuración de atajos de teclado
        self.root.bind('<Escape>', lambda e: self.root.quit())
        self.root.bind('c', lambda e: self.mark_task())  # Tecla 'C' para marcar como completada
        self.root.bind('u', lambda e: self.unmark_task())  # Tecla 'U' para desmarcar tarea
        self.root.bind('d', lambda e: self.delete_task())  # Tecla 'D' para eliminar
        self.root.bind('<Delete>', lambda e: self.delete_task())  # Tecla 'Delete' para eliminar
        self.root.bind('<Return>', lambda e: self.mark_task() if self.tasks.selection() else self.add_task())

        # Evento para añadir tarea con la tecla Enter
        self.task_entry.bind('<Return>', lambda event: self.add_task())

    def add_task(self):
        """Método para añadir una nueva tarea a la lista."""
        task = self.task_entry.get().strip()
        if task:
            self.tasks.insert('', tk.END, values=(task,))
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingresa una tarea.")

    def toggle_task_completion(self, event=None, complete=None):
        """Método para marcar o desmarcar una tarea como completada mediante doble clic."""
        selected_item = self.tasks.selection()
        if selected_item:
            for item in selected_item:
                task_text = self.tasks.item(item, 'values')[0]
                if task_text.startswith("✔ "):
                    self.tasks.item(item, values=(task_text.replace("✔ ", ""),))
                else:
                    self.tasks.item(item, values=(f"✔ {task_text}",))
        else:
            messagebox.showinfo("Información", "Selecciona una tarea para cambiar su estado.")

    def mark_task(self):
        """Método para marcar una tarea como completada."""
        selected_item = self.tasks.selection()
        if selected_item:
            for item in selected_item:
                task_text = self.tasks.item(item, 'values')[0]
                if not task_text.startswith("✔ "):
                    self.tasks.item(item, values=(f"✔ {task_text}",))
        else:
            messagebox.showinfo("Información", "Selecciona una tarea para marcar como completada.")

    def unmark_task(self):
        """Método para desmarcar una tarea completada."""
        selected_item = self.tasks.selection()
        if selected_item:
            for item in selected_item:
                task_text = self.tasks.item(item, 'values')[0]
                if task_text.startswith("✔ "):
                    self.tasks.item(item, values=(task_text.replace("✔ ", ""),))
        else:
            messagebox.showinfo("Información", "Selecciona una tarea para desmarcar.")

    def delete_task(self):
        """Método para eliminar la tarea seleccionada de la lista."""
        selected_item = self.tasks.selection()
        if selected_item:
            for item in selected_item:
                self.tasks.delete(item)
        else:
            messagebox.showinfo("Información", "Selecciona una tarea para eliminar.")


# Bloque principal para ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = TaskApp(root)
    root.mainloop()
