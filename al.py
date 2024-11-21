class Alumno:
    def __init__(self, nombre, apellido, edad, curso):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.curso = curso

    def programar(self):
        print(f"alumno {self.nombre} está programando.")

nombre = input("nombre del alumno: ").strip()
apellido = input("apellido del alumno: ").strip()
edad = input("edad del alumno: ").strip()
curso = input("curso del alumno: ").strip()

alumno = Alumno(nombre, apellido, edad, curso)
alumno.programar()
