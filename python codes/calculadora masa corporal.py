peso_kg = float(input("Ingrese su peso en kg: "))
print("")
estatura_m = float(input("Ingrese su altura en m: "))


imc = round(peso_kg/(estatura_m**2), 2)

print("")

print("Tu indice de masa corporal es ", imc)
