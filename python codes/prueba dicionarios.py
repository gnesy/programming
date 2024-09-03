
alumnos = []
nombre = str

while True:
    nombre = input("nombre: ")
    edad = input("edad: ")
    if nombre == '*':
        break

    alumnos.append((nombre, edad))

    print(alumnos)