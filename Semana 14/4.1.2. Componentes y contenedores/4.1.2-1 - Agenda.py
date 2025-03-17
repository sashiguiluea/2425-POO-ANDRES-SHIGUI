import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry


# Clase que representa un evento en la agenda.
class Evento:

    # Constructor de la clase Evento.
    # :param fecha: Fecha del evento.
    # :param hora: Hora del evento.
    # :param descripcion: Descripción del evento.
    def __init__(self, fecha, hora, descripcion):
        self.fecha = fecha
        self.hora = hora
        self.descripcion = descripcion


# Clase principal de la aplicación de agenda personal.
class AgendaApp:

    # Constructor de la clase AgendaApp.
    # :param root: Ventana principal de la aplicación.
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")  # Título de la ventana
        self.eventos = []  # Lista para almacenar eventos en memoria
        self.crear_interfaz()  # Llama al método para crear la interfaz gráfica

    # Crea la interfaz gráfica de la agenda.
    def crear_interfaz(self):
        # Frame para mostrar los eventos
        self.frame_events = ttk.Frame(self.root)
        self.frame_events.pack(pady=10, padx=10)

        # Treeview para mostrar los eventos en forma de tabla
        self.tree = ttk.Treeview(self.frame_events, columns=("Fecha", "Hora", "Descripción"), show="headings")
        for col in ("Fecha", "Hora", "Descripción"):
            self.tree.heading(col, text=col)  # Encabezados de las columnas
            self.tree.column(col, anchor="center", stretch=True)  # Alineación y ajuste de columnas
        self.tree.pack()

        # Frame para la entrada de nuevos eventos
        self.frame_input = ttk.LabelFrame(self.root, text="Nuevo Evento")
        self.frame_input.pack(pady=10, padx=10, fill="x")

        # Campo para seleccionar la fecha
        ttk.Label(self.frame_input, text="Fecha:").grid(row=0, column=0, padx=5, sticky="W")
        self.date_entry = DateEntry(self.frame_input, width=12, background='darkblue', foreground='white',
                                    borderwidth=2)
        self.date_entry.grid(row=0, column=1, padx=5, sticky="W")

        # Campos para seleccionar la hora
        ttk.Label(self.frame_input, text="Hora:").grid(row=1, column=0, padx=5, sticky="W")
        self.hour_spinbox = ttk.Spinbox(self.frame_input, from_=0, to=23, width=3, format="%02.0f", state='readonly')
        self.minute_spinbox = ttk.Spinbox(self.frame_input, from_=0, to=59, width=3, format="%02.0f", state='readonly')
        self.hour_spinbox.grid(row=1, column=1, padx=(5, 0), sticky="W")
        ttk.Label(self.frame_input, text=":").grid(row=1, column=1, padx=(40, 0), sticky="W")
        self.minute_spinbox.grid(row=1, column=1, padx=(55, 5), sticky="W")

        # Campo para la descripción del evento
        ttk.Label(self.frame_input, text="Descripción:").grid(row=2, column=0, padx=5, sticky="W")
        self.desc_entry = ttk.Entry(self.frame_input, width=40)
        self.desc_entry.grid(row=2, column=1, padx=5, sticky="W")

        # Frame para los botones de acción
        self.btn_frame = ttk.Frame(self.root)
        self.btn_frame.pack(pady=10)

        # Botones para agregar, eliminar y salir
        ttk.Button(self.btn_frame, text="Agregar Evento", command=self.agregar_evento).pack(side="left", padx=5)
        ttk.Button(self.btn_frame, text="Eliminar Evento Seleccionado", command=self.eliminar_evento).pack(side="left", padx=5)
        ttk.Button(self.btn_frame, text="Salir", command=self.root.quit).pack(side="left", padx=5)

        self.inicializar_tiempo()  # Inicializa los campos de hora y minuto

    # Inicializa los spinbox de hora y minuto en 00:00.
    def inicializar_tiempo(self):
        self.hour_spinbox.set("00")  # Establece la hora en 00
        self.minute_spinbox.set("00")  # Establece los minutos en 00

    # Agrega un nuevo evento a la agenda.
    def agregar_evento(self):
        fecha = self.date_entry.get()  # Obtiene la fecha del campo de entrada
        hora = f"{self.hour_spinbox.get()}:{self.minute_spinbox.get()}"  # Formatea la hora
        descripcion = self.desc_entry.get().strip()  # Obtiene la descripción y elimina espacios en blanco

        # Verifica que la descripción no esté vacía
        if not descripcion:
            messagebox.showwarning("Advertencia", "Por favor, ingrese una descripción.")
            return

        # Crea un nuevo evento y lo agrega a la lista
        evento = Evento(fecha, hora, descripcion)
        self.eventos.append(evento)
        self.tree.insert("", "end", values=(fecha, hora, descripcion))  # Inserta el evento en el Treeview
        self.limpiar_entradas()  # Limpia los campos de entrada

    # Elimina un evento seleccionado de la agenda.
    def eliminar_evento(self):
        seleccionado = self.tree.selection()  # Obtiene el evento seleccionado
        if not seleccionado:
            messagebox.showwarning("Advertencia", "Seleccione un evento para eliminar.")
            return

        # Confirma la eliminación del evento
        confirm = messagebox.askyesno("Confirmar", "¿Está seguro de que desea eliminar este evento?")
        if confirm:
            for item in seleccionado:
                valores = self.tree.item(item, "values")  # Obtiene los valores del evento seleccionado
                # Filtra la lista de eventos para eliminar el evento seleccionado
                self.eventos = [e for e in self.eventos if (e.fecha, e.hora, e.descripcion) != valores]
                self.tree.delete(item)  # Elimina el evento del Treeview

    # Limpia los campos de entrada.
    def limpiar_entradas(self):
        self.date_entry.set_date(self.date_entry.get_date())  # Restablece la fecha al valor actual
        self.inicializar_tiempo()  # Restablece la hora y los minutos a 00:00
        self.desc_entry.delete(0, tk.END)  # Limpia el campo de descripción


if __name__ == "__main__":
    root = tk.Tk()  # Crea la ventana principal
    app = AgendaApp(root)  # Inicializa la aplicación de agenda
    root.mainloop()  # Inicia el bucle principal de la interfaz gráfica