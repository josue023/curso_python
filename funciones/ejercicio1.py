# Escribe una función que calcule el área de un triángulo,
# recibiendo la altura y la base como parámetros y otra función que calcule el área de un círculo
# recibiendo el radio del mismo.


def areaTriangulo (base, altura):
    return (base * altura)/2

def areaCirculo (radio):
    return 3.1416 * radio**2

print("Area del triangulo: ", areaTriangulo(3, 4))

print("Area del circulo: ", areaCirculo(30))


