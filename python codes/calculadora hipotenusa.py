"""Haz una calculadora básica que permita 
realizar el cálculo de la hipotenusa de un
triángulo, vigilando que ningún cateto 
debe ser menor o igual a cero. 
Si se diera el caso, imprimir «Error» por
pantalla."""

from os import system
from math import sqrt

def calculo_hipotesuna(co, ca):
    hip = sqrt((pow(co, 2) + pow(ca, 2)))
    return hip

co=0
ca=0

while co<= 0 and ca<=0:
    
    print("""*Calculadora de la hipotenusa de un triangulo*
    """)
    co = float(input("Ingrese el cateto opuesto: "))
    ca = float(input("Ingrese el cateto adyacente: "))
    
    if co>0 and ca>0:
        print("La hipotenusa es ", round(calculo_hipotesuna(co, ca), 2))
        system("pause")
        system("cls")
    else: 
        
        print("""
        ¡¡¡ERROR: Los catetos son menores o iguales a 0!!!
        """)