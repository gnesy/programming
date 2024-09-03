import sqlite3

def servir_cafe(opcion):
	if opcion==1:
		print("Ay vale, cafe con lechita")
		with sqlite3.connect("cafe.db") as conn:
			cursor = conn.cursor()
			consulta = """INSERT INTO Cafe VALUES (?, ?)"""
			cursor.execute(consulta,(1, "Cafe con leche"))
			conn.commit()
	elif opcion==2:
		with sqlite3.connect("cafe.db") as conn:
			cursor = conn.cursor()
			consulta = """INSERT INTO Cafe VALUES (?, ?)"""
			cursor.execute(consulta,(2, "Cafe pruo duro de la mata"))
			conn.commit()
		print("Eres todo un hombre vale")
	elif opcion==3:
		with sqlite3.connect("cafe.db") as conn:
			cursor = conn.cursor()
			consulta = """INSERT INTO Cafe VALUES (?, ?)"""
			cursor.execute(consulta,(3, "Cafe instantáneo"))
			conn.commit()
		print("Cafe")

def validar_cafe():
	print("1. Cafe con leche")
	print("2. Cafe puro duro de la mata")
	print("3. Cafe instantáneo")
	opcion = int(input("\n\nOpción: "))
	servir_cafe(opcion)

def pedir_cafe():
	cafe = input("¿Quieres un café?: ")
	if cafe.lower()=='si':
		validar_cafe()
	elif cafe.lower()=='no':
		print("\nEntonces a qué viniste.")
	else:
		print("QUÉ")

def main():
	pedir_cafe()

if __name__ == '__main__':
	main()