#lista de alumnos
alumnos = []
def agregar_alumno(nombre, edad):
    alumnos.append({'nombre': nombre, 'edad': edad})

def mayores_de_edad():
    return[alumno for alumno in alumnos if alumno['edad']>=18]

def alumno_mayor():
    return max(alumnos, key=lambda item: item['edad'])

while True:
    nombre= input("Introduce el nombre del pobre pendejo o presione * para termina: ")
    if nombre== '*':
        break
try:
    edad = int(input("Introduce la edad del pobre pendejo:"))
    agregar_alumno(nombre,edad)
except ValueError:
    print("Por favor no seas pendejo introduce un numero valido")

print("Pobre pendejos mayores de edad:")
for alumno in mayores_de_edad():
    print(f"{alumno['nombre']} - {alumno['edad']} años")

mayor = alumno_mayor()
print(f"El pobre pendejo mayor edad es: {mayor['nombre']} con {mayor['edad']} años")