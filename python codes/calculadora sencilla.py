"""Haz una calculadora básica pida al usuario dos valores, a y b.

Según la opción que desean, realizar la operación:

Si operación es 1 entonces debemos ver el resultado de a + b
Si operación es 2 entonces debemos ver el resultado de a * b
Si operación es 3 entonces debemos ver el resultado de a - b
Si operación es 4 entonces debemos ver el resultado de a / b
Si operación es 5 entonces debemos ver el resultado de a**n
Si operación es 6 entonces debemos ver el resultado de a!"""

from os import system 
from math import pow

def suma(a, b):
    return float(a+b)

def resta(a, b):
    return a-b

def multiplicacion(a, b):
    return a*b

def division(a, b):
    return a/b

def potencia(a, n):
    return pow(a, n)

def factorial(a):
    i=1
    for i in range(1, a):
        a = a*i
        print(a)
    return a

print("""
    ***Calculadora***
    
[1]. Suma de 2 numeros [+]
[2]. Resta de 2 numeros [-]
[3]. Multiplicacion de 2 numeros [*]
[4]. Division de 2 numeros [/]
[5]. Potencia de un numero [**]
[6]. El factorial de un numero [!]
---------------------""")
op = int(input("Elija una opcion: "))

if op == 1:
    a = float(input("Ingrese el primer numero:"))
    b = float(input("Ingrese el segundo numero: "))
    
    print(suma(a, b))
    
    system("pause")
    system("cls")
elif op == 2:
    a = float(input("Ingrese el primer numero:"))
    b = float(input("Ingrese el segundo numero: "))
    
    print(resta(a, b))
    
    system("pause")
    system("cls")
elif op == 3:
    a = float(input("Ingrese el primer numero:"))
    b = float(input("Ingrese el segundo numero: "))
    
    print(multiplicacion(a, b))
    
    system("pause")
    system("cls")
elif op == 4:
    a = float(input("Ingrese el primer numero:"))
    b = float(input("Ingrese el segundo numero: "))
    
    print(division(a, b))
    
    system("pause")
    system("cls")
elif op == 5: 
    a = float(input("Ingrese el numero: "))
    n = int(input("Ingrese la pontencia del numero: "))
    
    print(potencia(a, n))
    
    system("pause")
    system("cls")
elif op == 6:
    a = int(input("Ingrese el numero:"))
    
    print(factorial(a))
    
    system("pause")
    system("cls")
else: 
    print ("""
        Error: Elija una de las opciones anteriores
        """)