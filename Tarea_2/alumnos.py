class alumno:
    def __init__(self, nombre, apellido, edad, nota, nacionalidad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.nota = nota
        self.nacionalidad = nacionalidad
    
    def leerNota(self):
        print(f"La nota es: {self.nota}")

    def registrarNota(self, nota):
        self.nota = nota
