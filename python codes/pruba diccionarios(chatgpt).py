# Inicializamos una lista para almacenar los datos de los alumnos
alumnos = []

# Variable para almacenar la edad máxima
edad_maxima = 0

# Variable para almacenar los alumnos mayores
alumnos_mayores = []

# Solicitamos al usuario que introduzca nombre y edad de los alumnos
while True:
    nombre = input("Introduce el nombre del alumno (o '*' para salir): ")
    
    # Comprobamos si se quiere salir del programa
    if nombre == '*':
        break
    
    edad = int(input("Introduce la edad de {}:".format(nombre)))
    
    # Guardamos los datos del alumno en la lista de alumnos
    alumnos.append((nombre, edad))
    
    # Actualizamos la edad máxima
    if edad > edad_maxima:
        edad_maxima = edad
        alumnos_mayores = [(nombre, edad)]
    elif edad == edad_maxima:
        alumnos_mayores.append((nombre, edad))

# Mostramos los alumnos mayores de edad
print("\nAlumnos mayores de edad:")
for nombre, edad in alumnos:
    if edad >= 18:
        print("- Nombre: {}, Edad: {}".format(nombre, edad))

# Mostramos los alumnos mayores
print("\nAlumnos mayores:")
for nombre, edad in alumnos_mayores:
    print("- Nombre: {}, Edad: {}".format(nombre, edad))
