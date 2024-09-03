print("**********************")
print("**   CONVERSOR DE   **")
print("**DOLARES A BOLIVARES**")
print("**BOLIVARES A DOLARES**")
print("***********************")
print("")
print("Elije una opción:\n")


opción = int(input("1-. Dolares a Bolivares o 2-. Bolivares a Dolares: "))
print("")
if opción == 1:
    dolares = float(input("Ingrese la cantidad en dolares que desea convertir: "))
    print("")
    bolivares = 36.31
    total_bolivares = dolares*bolivares
    print(dolares, "$", "son", round(total_bolivares, 2), "bs")
elif opción == 2:
	bolivares = float(input("Ingrese la cantidad en bolivares que desea convertir: "))
	print("")
	dolares = 36.31
	total_dolares = bolivares/dolares
	print(bolivares, "bs", "son", round(total_dolares, 2), "$")
else: 
	print("*Opción no valida*\n")

