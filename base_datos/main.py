import sqlite3

def buscarAlumno(nombre):

    conn = sqlite3.connect("escuela.db")
    cursor = conn.cursor()

    query = f"SELECT * FROM alumno WHERE nombre='{nombre}'"
    rows = cursor.execute(query)

    data = rows.fetchone()

    if data != None:
        print(data)
    else:
        print("Este alumno no existe en la base de datos")

    cursor.close()
    conn.close()

def main():
    nombre = input("Ingrese el nombre del alumno: ")

    buscarAlumno(nombre)


if __name__ == "__main__":
    main()