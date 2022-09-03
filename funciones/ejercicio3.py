# Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.

def anioBisiesto(anio):
    if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
        return "año bisiesto"

    return "no es bisiesto este año"


print(anioBisiesto(2024))
