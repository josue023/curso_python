# En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno
# que tenga como atributos su nombre y su nota.
# Deberéis de definir los métodos para inicializar sus atributos,
# imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.


class Alumno:
    nombre = ""
    nota = 0

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def isEstado(self):

        if self.nota >= 7 :
            return "Aprobado"

        return "Reprobado"


a = Alumno("Caleb", 6.9)

print(a.nombre)
print(a.nota)
print(a.isEstado())