"""
Pedir su nombre al usuario en MAYÚSCULA, 
si su nombre comienza por la letra A, 
convertir su nombre a minúsculas y finalizar
el programa, en caso de no ingresar el nombre
en MAYÚSCULAS el programa debe pedir nuevamente
el ingreso del nombre hasta que este se ingrese
en mayúsculas.
"""
from os import system

def main():
	nombre = "a"
	while nombre!=nombre.upper():
		nombre = input("Ingresa tu nombre en mayúsculas: ")
		if nombre == nombre.upper():
			if nombre[0] == "A":
				print("Su nombre es " + nombre.lower())
			else:
				print("Su nombre es " + nombre)
		else:
			print("Por favor, el nombre debe ir en mayúsculas")
		
		system("pause")
		system("cls")


if __name__ == '__main__':
	main()