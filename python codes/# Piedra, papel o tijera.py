# Piedra, papel o tijera

import random
jugadas = ["piedra", "papel", "tijera"]

jugador = input("Introduce tu jugada (piedra, papel o tijera): ")
maquina = random.choice(jugadas)

print("La máquina ha elegido", maquina)

if jugador == maquina:
    print("Empate!")
elif jugador == "piedra" and maquina == "papel":
    print("La máquina gana!")
elif jugador == "piedra" and maquina == "tijera":
    print("¡Tú ganas!")
elif jugador == "papel" and maquina == "piedra":
    print("¡Tú ganas!")
elif jugador == "papel" and maquina == "tijera":
    print("La máquina gana!")
elif jugador == "tijera" and maquina == "piedra":
    print("La máquina gana!")
elif jugador == "tijera" and maquina == "papel":
    print("¡Tú ganas!")
