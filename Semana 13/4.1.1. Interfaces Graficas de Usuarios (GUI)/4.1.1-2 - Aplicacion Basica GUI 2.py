import tkinter as tk
from tkinter import ttk, messagebox

# Funciones para la aplicación
def agregar():
    """
    Agrega la información ingresada en los campos de texto a la tabla.
    Valida que los campos no estén vacíos y que el teléfono contenga solo números.
    """
    nombre = entrada_nombre.get().strip()
    direccion = entrada_direccion.get().strip()
    telefono = entrada_telefono.get().strip()

    # Validar que todos los campos estén llenos
    if not nombre or not direccion or not telefono:
        messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")
        return

    # Validar que el número de teléfono contenga solo dígitos
    if not telefono.isdigit():
        messagebox.showwarning("Advertencia", "El teléfono debe contener solo números.")
        return

    # Insertar datos en la tabla
    tree.insert("", tk.END, values=(nombre, direccion, telefono))

    # Limpiar los campos de entrada después de agregar
    limpiar_campos()

def eliminar():
    """
    Elimina el elemento seleccionado en la tabla.
    Muestra un mensaje de advertencia si no hay selección.
    """
    seleccionado = tree.selection()  # Obtener los elementos seleccionados
    if not seleccionado:
        messagebox.showwarning("Advertencia", "Debe seleccionar un elemento para eliminar.")
        return

    # Eliminar cada elemento seleccionado
    for item in seleccionado:
        tree.delete(item)

def limpiar():
    """
    Elimina todos los elementos de la tabla.
    """
    for item in tree.get_children():
        tree.delete(item)

def limpiar_campos():
    """
    Borra los datos de los campos de entrada sin afectar la tabla.
    """
    entrada_nombre.delete(0, tk.END)
    entrada_direccion.delete(0, tk.END)
    entrada_telefono.delete(0, tk.END)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación Básica GUI con Tabla")  # Título de la ventana
ventana.geometry("600x400")  # Tamaño inicial de la ventana

# Menú superior
menu = tk.Menu(ventana)
ventana.config(menu=menu)

# Submenú "Archivo" con opciones de agregar, limpiar y salir
archivo_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Archivo", menu=archivo_menu)
archivo_menu.add_command(label="Agregar", command=agregar)
archivo_menu.add_command(label="Limpiar Todo", command=limpiar)
archivo_menu.add_separator()
archivo_menu.add_command(label="Salir", command=ventana.quit)

# Marco para organizar los campos de entrada y botones
frame = tk.Frame(ventana)
frame.pack(pady=10)

# Etiquetas y campos de entrada de datos
tk.Label(frame, text="Nombre:").grid(row=0, column=0, sticky="e")
entrada_nombre = tk.Entry(frame)
entrada_nombre.grid(row=0, column=1)

tk.Label(frame, text="Dirección:").grid(row=1, column=0, sticky="e")
entrada_direccion = tk.Entry(frame)
entrada_direccion.grid(row=1, column=1)

tk.Label(frame, text="Teléfono:").grid(row=2, column=0, sticky="e")
entrada_telefono = tk.Entry(frame)
entrada_telefono.grid(row=2, column=1)

# Botón para agregar datos a la tabla
boton_agregar = tk.Button(frame, text="Agregar", command=agregar)
boton_agregar.grid(row=3, column=0, columnspan=2, pady=5)

# Botón para eliminar el elemento seleccionado de la tabla
boton_eliminar = tk.Button(frame, text="Eliminar Seleccionado", command=eliminar)
boton_eliminar.grid(row=4, column=0, columnspan=2, pady=5)

# Botón para limpiar todos los datos de la tabla
boton_limpiar = tk.Button(frame, text="Limpiar Todo", command=limpiar)
boton_limpiar.grid(row=5, column=0, columnspan=2, pady=5)

# Tabla (Treeview) para mostrar los datos ingresados
tree = ttk.Treeview(ventana, columns=("Nombre", "Dirección", "Teléfono"), show="headings")

# Definir encabezados de las columnas
tree.heading("Nombre", text="Nombre")
tree.heading("Dirección", text="Dirección")
tree.heading("Teléfono", text="Teléfono")

# Expandir la tabla para que ocupe todo el ancho de la ventana
tree.pack(pady=10, fill=tk.BOTH, expand=True)

# Iniciar el bucle principal
ventana.mainloop()