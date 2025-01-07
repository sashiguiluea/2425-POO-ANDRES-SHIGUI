# Clase que representa un Alumno
class Alumno:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre  # Nombre del alumno.
        self.apellido = apellido  # Apellido del alumno.
        self.edad = edad  # Edad del alumno.

    def __str__(self):
        # Devuelve una representación en texto del alumno, mostrando su nombre completo y edad.
        return f'{self.nombre} {self.apellido} {self.edad}'

# Clase que representa a un curso de un alumno
class Curso:
    def __init__(self, nombre):
        self.nombre = nombre  # Nombre del curso.
        self.alumnos = []  # Lista para almacenar los alumnos matriculados en el curso.

    def __str__(self):
        # Devuelve el nombre del curso como representación en texto.
        return self.nombre

    def matricular_alumno(self, alumno):
        # Método para agregar un alumno a la lista de alumnos del curso.
        self.alumnos.append(alumno)

    def anular_matricular(self, alumno):
        # Método para eliminar un alumno de la lista de alumnos del curso.
        self.alumnos.remove(alumno)

    def edad_media_alumnos(self):
        # Método para calcular la edad media de los alumnos matriculados.
        media = 0
        for alumno in self.alumnos:  # Recorre cada alumno en la lista.
            media += alumno.edad  # Suma la edad de cada alumno.
        media = media / len(self.alumnos)  # Divide la suma total por la cantidad de alumnos.
        return media  # Devuelve la edad media.

    def mostrar_alumnos(self):
        # Método para imprimir la lista de alumnos matriculados en el curso.
        print("Alumnos del curso {}:".format(self))  # Imprime el nombre del curso.
        for alumno in self.alumnos:  # Recorre cada alumno en la lista.
            print("-", alumno)  # Muestra la información de cada alumno.

# Crear un curso llamado "Astronomía".
astronomia = Curso("Astronomia")

# Crear alumnos.
andres = Alumno("Andrés", "Shigui", 27)  # Alumno llamado Andrés con 27 años.
alejandra = Alumno("Alejandra", "Shigui", 17)  # Alumna llamada Alejandra con 17 años.
marisol = Alumno("Marisol", "Shigui", 20)  # Alumna llamada Marisol con 20 años.

# Matricular alumnos en el curso.
astronomia.matricular_alumno(andres)  # Matricula a Andrés.
astronomia.matricular_alumno(alejandra)  # Matricula a Alejandra.
astronomia.matricular_alumno(marisol)  # Matricula a Marisol.

# Anular la matrícula de Alejandra.
astronomia.anular_matricular(alejandra)

# Mostrar la lista de alumnos actualmente matriculados.
astronomia.mostrar_alumnos()

# Mostrar la edad media de los alumnos en el curso.
print("Edad media curso {}: ".format(astronomia), end="")  # Muestra un encabezado.
print(astronomia.edad_media_alumnos())  # Calcula y muestra la edad media.
