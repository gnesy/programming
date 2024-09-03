"""Determinar si alguien es menor de edad o no. Pide al usuario
la edad por pantalla e imprime por pantalla si puede acceder a nuestra 
fiesta nocturna de BigBayData.com."""
from os import system
edad=0
while edad <= 18:
    edad = int(input("how old are you?: "))
    if edad >= 18:
        print("welcome to the party!!!!")
        system("pause")
        system("cls")
    else: 
        print("bye bye little boy :'(")