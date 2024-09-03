import random

# Creamos un conjunto con los números del 0 al 7
conjunto_numeros = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E','F'}
# Definimos la función para generar una secuencia aleatoria de 4 cifras
def generar_secuencia():
    secuencia = []
    for i in range(4):
    # Elegimos un número aleatorio del conjunto
        numero_aleatorio = random.choice(list(conjunto_numeros))
    # Agregamos el número aleatorio a la secuencia
        secuencia.append(numero_aleatorio)
    # Devolvemos la secuencia como una cadena
    return "".join(str(numero) for numero in secuencia)

# Generamos y mostramos dos secuencias aleatorias de 4 cifras
secuencia1 = generar_secuencia()
secuencia2 = generar_secuencia()

print(f"Primera secuencia: {secuencia1}")
print(f"Segunda secuencia: {secuencia2}")
