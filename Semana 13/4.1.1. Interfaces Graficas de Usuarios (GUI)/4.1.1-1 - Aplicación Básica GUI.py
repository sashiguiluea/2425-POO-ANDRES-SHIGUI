import tkinter as tk
from tkinter import ttk, messagebox

class AplicacionGUI:
    """
    Clase que define una aplicación de interfaz gráfica de usuario (GUI) usando Tkinter.
    Permite agregar, eliminar y visualizar información en una tabla.
    """

    def __init__(self, ventana):
        """
        Inicializa la ventana principal y todos los elementos de la GUI.
        :param ventana: Instancia de Tkinter.Tk() que representa la ventana principal.
        """
        self.ventana = ventana
        self.ventana.title("Aplicación Básica GUI con Tabla")  # Título de la ventana
        self.ventana.geometry("600x400")  # Tamaño inicial de la ventana

        # Menú superior
        self.menu = tk.Menu(self.ventana)
        self.ventana.config(menu=self.menu)

        # Submenú "Archivo" con opciones de agregar, limpiar y salir
        self.archivo_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Archivo", menu=self.archivo_menu)
        self.archivo_menu.add_command(label="Agregar", command=self.agregar)
        self.archivo_menu.add_command(label="Limpiar Todo", command=self.limpiar)
        self.archivo_menu.add_separator()
        self.archivo_menu.add_command(label="Salir", command=self.ventana.quit)

        # Marco para organizar los campos de entrada y botones
        self.frame = tk.Frame(ventana)
        self.frame.pack(pady=10)

        # Etiquetas y campos de entrada de datos
        tk.Label(self.frame, text="Nombre:").grid(row=0, column=0, sticky="e")
        self.entrada_nombre = tk.Entry(self.frame)
        self.entrada_nombre.grid(row=0, column=1)

        tk.Label(self.frame, text="Dirección:").grid(row=1, column=0, sticky="e")
        self.entrada_direccion = tk.Entry(self.frame)
        self.entrada_direccion.grid(row=1, column=1)

        tk.Label(self.frame, text="Teléfono:").grid(row=2, column=0, sticky="e")
        self.entrada_telefono = tk.Entry(self.frame)
        self.entrada_telefono.grid(row=2, column=1)

        # Botón para agregar datos a la tabla
        self.boton_agregar = tk.Button(self.frame, text="Agregar", command=self.agregar)
        self.boton_agregar.grid(row=3, column=0, columnspan=2, pady=5)

        # Botón para eliminar el elemento seleccionado de la tabla
        self.boton_eliminar = tk.Button(self.frame, text="Eliminar Seleccionado", command=self.eliminar)
        self.boton_eliminar.grid(row=4, column=0, columnspan=2, pady=5)

        # Botón para limpiar todos los datos de la tabla
        self.boton_limpiar = tk.Button(self.frame, text="Limpiar Todo", command=self.limpiar)
        self.boton_limpiar.grid(row=5, column=0, columnspan=2, pady=5)

        # Tabla (Treeview) para mostrar los datos ingresados
        self.tree = ttk.Treeview(ventana, columns=("Nombre", "Dirección", "Teléfono"), show="headings")

        # Definir encabezados de las columnas
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Dirección", text="Dirección")
        self.tree.heading("Teléfono", text="Teléfono")

        # Expandir la tabla para que ocupe todo el ancho de la ventana
        self.tree.pack(pady=10, fill=tk.BOTH, expand=True)

    def agregar(self):
        """
        Agrega la información ingresada en los campos de texto a la tabla.
        Valida que los campos no estén vacíos y que el teléfono contenga solo números.
        """
        nombre = self.entrada_nombre.get().strip()
        direccion = self.entrada_direccion.get().strip()
        telefono = self.entrada_telefono.get().strip()

        # Validar que todos los campos estén llenos
        if not nombre or not direccion or not telefono:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")
            return

        # Validar que el número de teléfono contenga solo dígitos
        if not telefono.isdigit():
            messagebox.showwarning("Advertencia", "El teléfono debe contener solo números.")
            return

        # Insertar datos en la tabla
        self.tree.insert("", tk.END, values=(nombre, direccion, telefono))

        # Limpiar los campos de entrada después de agregar
        self.limpiar_campos()

    def eliminar(self):
        """
        Elimina el elemento seleccionado en la tabla.
        Muestra un mensaje de advertencia si no hay selección.
        """
        seleccionado = self.tree.selection()  # Obtener los elementos seleccionados
        if not seleccionado:
            messagebox.showwarning("Advertencia", "Debe seleccionar un elemento para eliminar.")
            return

        # Eliminar cada elemento seleccionado
        for item in seleccionado:
            self.tree.delete(item)

    def limpiar(self):
        """
        Elimina todos los elementos de la tabla.
        """
        for item in self.tree.get_children():
            self.tree.delete(item)

    def limpiar_campos(self):
        """
        Borra los datos de los campos de entrada sin afectar la tabla.
        """
        self.entrada_nombre.delete(0, tk.END)
        self.entrada_direccion.delete(0, tk.END)
        self.entrada_telefono.delete(0, tk.END)

if __name__ == "__main__":
    # Crear y ejecutar la ventana de la aplicación
    ventana = tk.Tk()
    app = AplicacionGUI(ventana)
    ventana.mainloop()
