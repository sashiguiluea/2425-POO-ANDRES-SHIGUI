import tkinter as tk
from tkinter import messagebox, ttk


# Clase que representa la aplicación de gestión de tareas
class TaskApp:
    def __init__(self, root):
        """Inicializa la interfaz gráfica y sus componentes."""
        self.root = root
        self.root.title("Gestión de Tareas")  # Título de la ventana
        self.root.geometry("500x500")  # Tamaño de la ventana

        # Configuración de estilos para la vista de tareas
        self.style = ttk.Style()
        self.style.configure("Treeview", rowheight=25)

        # Campo de entrada para añadir nuevas tareas
        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.pack(pady=10)

        # Botón para añadir una nueva tarea a la lista
        self.add_button = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(pady=5)

        # Lista de tareas utilizando Treeview de ttk
        self.tasks = ttk.Treeview(root, columns=("Tarea"), show='headings', selectmode='browse')
        self.tasks.heading("Tarea", text="Descripción")  # Encabezado de la lista
        self.tasks.pack(fill=tk.BOTH, expand=True, pady=10)

        # Configuración de estilos para diferenciar tareas completadas y pendientes
        self.tasks.tag_configure("completed", foreground="green", font=("Arial", 10, "italic"), background="#d4f8d4")
        self.tasks.tag_configure("pending", foreground="black", font=("Arial", 10, "normal"))

        # Asigna el evento de doble clic para marcar/desmarcar tareas como completadas
        self.tasks.bind("<Double-1>", self.toggle_task_completion)

        # Contenedor para los botones de acciones
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        # Botón para marcar una tarea como completada
        self.complete_button = tk.Button(button_frame, text="Marcar Completada", command=self.mark_task)
        self.complete_button.grid(row=0, column=0, padx=5)

        # Botón para eliminar una tarea seleccionada
        self.delete_button = tk.Button(button_frame, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.grid(row=0, column=1, padx=5)

        # Configuración de atajos de teclado
        self.root.bind("<Escape>", lambda e: self.root.quit())  # Salir con la tecla Escape
        self.root.bind("c", lambda e: self.mark_task())  # Marcar tarea con la tecla 'C'
        self.root.bind("d", lambda e: self.delete_task())  # Eliminar tarea con la tecla 'D'
        self.root.bind("<Delete>", lambda e: self.delete_task())  # Eliminar tarea con la tecla 'Delete'
        self.task_entry.bind("<Return>", lambda event: self.add_task())  # Añadir tarea con la tecla Enter

    def add_task(self):
        """Añade una nueva tarea a la lista si el campo de entrada no está vacío."""
        task = self.task_entry.get().strip()
        if task:
            self.tasks.insert("", tk.END, values=(task,), tags=("pending",))  # Se inserta como pendiente
            self.task_entry.delete(0, tk.END)  # Limpia el campo de entrada
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingresa una tarea.")  # Muestra advertencia si está vacío

    def toggle_task_completion(self, event=None):
        """Cambia el estado de la tarea seleccionada entre pendiente y completada."""
        selected_item = self.tasks.selection()
        if selected_item:
            for item in selected_item:
                task_text = self.tasks.item(item, "values")[0]
                if task_text.startswith("✔ "):
                    self.tasks.item(item, values=(task_text.replace("✔ ", ""),))  # Quita el check
                    self.tasks.item(item, tags=("pending",))  # Cambia el estilo a pendiente
                else:
                    self.tasks.item(item, values=(f"✔ {task_text}",))  # Añade el check
                    self.tasks.item(item, tags=("completed",))  # Cambia el estilo a completado
            # Reaplica la configuración de estilos
            self.tasks.tag_configure("completed", foreground="green", font=("Arial", 10, "italic"),
                                     background="#d4f8d4")
            self.tasks.tag_configure("pending", foreground="black", font=("Arial", 10, "normal"))
        else:
            messagebox.showinfo("Información", "Selecciona una tarea para cambiar su estado.")

    def mark_task(self):
        """Marca la tarea seleccionada como completada."""
        selected_item = self.tasks.selection()
        if selected_item:
            for item in selected_item:
                task_text = self.tasks.item(item, "values")[0]
                if not task_text.startswith("✔ "):
                    self.tasks.item(item, values=(f"✔ {task_text}",))  # Añade el check
                    self.tasks.item(item, tags=("completed",))  # Cambia el estilo a completado
            self.tasks.tag_configure("completed", foreground="green", font=("Arial", 10, "italic"),
                                     background="#d4f8d4")
        else:
            messagebox.showinfo("Información", "Selecciona una tarea para marcar como completada.")

    def delete_task(self):
        """Elimina la tarea seleccionada de la lista."""
        selected_item = self.tasks.selection()
        if selected_item:
            for item in selected_item:
                self.tasks.delete(item)  # Elimina la tarea
        else:
            messagebox.showinfo("Información", "Selecciona una tarea para eliminar.")


# Bloque principal para ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = TaskApp(root)
    root.mainloop()
