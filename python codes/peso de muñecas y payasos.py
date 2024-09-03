peso_pasayo = 122
peso_muñeca = 75

print("**Registo del ultimo pedido**\n")

payaso_venta = int(input("Ingrese la cantidad de payasos vendidos: \n"))
print("")
muñeca_venta = int(input("Ingrese la cantidad de muñecas vendidad: "))
print("")

peso_total = round(((peso_muñeca * muñeca_venta) + (peso_pasayo * payaso_venta)), 2)

peso_total = round((peso_total/1000), 2)
print("El peso total del ultimo pedido en kilogramos (kg): ", peso_total)
