import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

# Lista para almacenar eventos en memoria
eventos = []

# Función para crear la interfaz gráfica de la agenda
def crear_interfaz(root):
    # Frame para mostrar los eventos
    frame_events = ttk.Frame(root)
    frame_events.pack(pady=10, padx=10)

    # Treeview para mostrar los eventos en forma de tabla
    tree = ttk.Treeview(frame_events, columns=("Fecha", "Hora", "Descripción"), show="headings")
    for col in ("Fecha", "Hora", "Descripción"):
        tree.heading(col, text=col)  # Encabezados de las columnas
        tree.column(col, anchor="center", stretch=True)  # Alineación y ajuste de columnas
    tree.pack()

    # Frame para la entrada de nuevos eventos
    frame_input = ttk.LabelFrame(root, text="Nuevo Evento")
    frame_input.pack(pady=10, padx=10, fill="x")

    # Campo para seleccionar la fecha
    ttk.Label(frame_input, text="Fecha:").grid(row=0, column=0, padx=5, sticky="W")
    date_entry = DateEntry(frame_input, width=12, background='darkblue', foreground='white', borderwidth=2)
    date_entry.grid(row=0, column=1, padx=5, sticky="W")

    # Campo para ingresar la hora
    ttk.Label(frame_input, text="Hora (HH:MM):").grid(row=1, column=0, padx=5, sticky="W")
    hour_entry = ttk.Entry(frame_input, width=5)
    hour_entry.grid(row=1, column=1, padx=5, sticky="W")

    # Campo para la descripción del evento
    ttk.Label(frame_input, text="Descripción:").grid(row=2, column=0, padx=5, sticky="W")
    desc_entry = ttk.Entry(frame_input, width=40)
    desc_entry.grid(row=2, column=1, padx=5, sticky="W")

    # Frame para los botones de acción
    btn_frame = ttk.Frame(root)
    btn_frame.pack(pady=10)

    # Botones para agregar, eliminar y salir
    ttk.Button(btn_frame, text="Agregar Evento", command=lambda: agregar_evento(tree, date_entry, hour_entry, desc_entry)).pack(side="left", padx=5)
    ttk.Button(btn_frame, text="Eliminar Evento Seleccionado", command=lambda: eliminar_evento(tree)).pack(side="left", padx=5)
    ttk.Button(btn_frame, text="Salir", command=root.quit).pack(side="left", padx=5)

# Función para agregar un nuevo evento a la agenda
def agregar_evento(tree, date_entry, hour_entry, desc_entry):
    fecha = date_entry.get()  # Obtiene la fecha del campo de entrada
    hora = hour_entry.get().strip()  # Obtiene la hora del campo de entrada
    descripcion = desc_entry.get().strip()  # Obtiene la descripción y elimina espacios en blanco

    # Verifica que la descripción y la hora no estén vacías
    if not descripcion:
        messagebox.showwarning("Advertencia", "Por favor, ingrese una descripción.")
        return
    if not hora or len(hora) != 5 or hora[2] != ':' or not hora[:2].isdigit() or not hora[3:].isdigit():
        messagebox.showwarning("Advertencia", "Por favor, ingrese una hora válida en formato HH:MM.")
        return

    # Crea un nuevo evento y lo agrega a la lista
    evento = (fecha, hora, descripcion)
    eventos.append(evento)
    tree.insert("", "end", values=evento)  # Inserta el evento en el Treeview
    limpiar_entradas(date_entry, hour_entry, desc_entry)  # Limpia los campos de entrada

# Función para eliminar un evento seleccionado de la agenda
def eliminar_evento(tree):
    seleccionado = tree.selection()  # Obtiene el evento seleccionado
    if not seleccionado:
        messagebox.showwarning("Advertencia", "Seleccione un evento para eliminar.")
        return

    # Confirma la eliminación del evento
    confirm = messagebox.askyesno("Confirmar", "¿Está seguro de que desea eliminar este evento?")
    if confirm:
        for item in seleccionado:
            valores = tree.item(item, "values")  # Obtiene los valores del evento seleccionado
            # Filtra la lista de eventos para eliminar el evento seleccionado
            global eventos
            eventos = [e for e in eventos if e != valores]
            tree.delete(item)  # Elimina el evento del Treeview

# Función para limpiar los campos de entrada
def limpiar_entradas(date_entry, hour_entry, desc_entry):
    date_entry.set_date(date_entry.get_date())  # Restablece la fecha al valor actual
    hour_entry.delete(0, tk.END)  # Limpia el campo de hora
    desc_entry.delete(0, tk.END)  # Limpia el campo de descripción

if __name__ == "__main__":
    root = tk.Tk()  # Crea la ventana principal
    root.title("Agenda Personal")  # Título de la ventana
    crear_interfaz(root)  # Crea la interfaz gráfica
    root.mainloop()  # Inicia el bucle principal de la interfaz gráfica ```python