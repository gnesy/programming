"""1) Este programa pide primeramente la cantidad total de 
compras de una persona. Si la cantidad es inferior a $100.00,
el programa dirá que el cliente no aplica a la promoción. 
Pero si la persona ingresa una cantidad en compras igual o 
superior a $100.00, el programa genera de forma aleatoria 
un número entero del cero al cinco. Cada número corresponderá 
a un color diferente de cinco colores de bolas que hay para
determinar el descuento que el cliente recibirá como premio.
Si la bola aleatoria es color blanco, no hay descuento,
pero si es uno de los otros cuatro colores, sí se aplicará
un descuento determinado según la tabla que  aparecerá, 
y ese descuento se aplicará sobre el total de compra que
introdujo inicialmente el usuario, de manera que el programa
mostrará un nuevo valor a pagar luego de haber aplicado el 
descuento"""

import random
from os import system

def amarillo(monto):
    descuento = (monto * (5/100))
    monto_final = monto - descuento
    return monto_final

def verde(monto):
    descuento = (monto * (10/100))
    monto_final = monto - descuento
    return monto_final

def azul(monto):
    descuento = (monto * (20/100))
    monto_final = monto - descuento
    return monto_final

def morado(monto):
    descuento = (monto * (50/100))
    monto_final = monto - descuento
    return monto_final

def naranja(monto):
    descuento = (monto * (100/100))
    monto_final = monto - descuento
    return monto_final

monto = float
bolas = [0, 1, 2, 3, 4, 5]
while monto != 0: 
    
    monto = float(input("""
    Ingrese su monto a pagar y ruegue que tenga un descuento: """))
    print("")
    
    descuento_final = [random.choice(bolas)]
    
    if monto >= 100.00:
        if descuento_final[0] == 1:
            
            print(f"""Le ha tocado la bola amarilla
            Su descuento es de 5%
            -Su monto a pagar es {amarillo(monto)}""")
            system("pause")
            system("cls")
            
        elif descuento_final[0] == 2:
            
            print(f"""Le ha tocado la bola verde
            Su descuento es de 10%
            -Su monto a pagar es {verde(monto)}""")
            system("pause")
            system("cls")
            
        elif descuento_final[0] == 3:
            
            print(f"""Le ha tocado la bola azul
            Su descuento es de 20%
            -Su monto a pagar es {azul(monto)}""")
            system("pause")
            system("cls")
            
        elif descuento_final[0] == 4:
            
            print(f"""Le ha tocado la bola morada
            Su descuento es de 50%
            -Su monto a pagar es {morado(monto)}""")
            system("pause")
            system("cls")
            
        elif descuento_final[0] == 5: 
            
            print(f"""Le ha tocado la bola naranja
            Su descuento es de 100%
            FELICIDADES!!
            -Su monto a pagar es {naranja(monto)}, no pagas nada miamol""")
            system("pause")
            system("cls")
            
        elif descuento_final[0] == 0:
            
            print(f"""Le ha tocado la bola blanca
            NO tiene descuento, que mala suerte
            -Su monto a pagar es {monto}""")
            system("pause")
            system("cls")
            
    elif monto == 0:
        print("""ADIOOOS!
        """)
        system("pause")
        system("cls")
        break
    else: 
        print("""
        *Este monto no aplica para un descuento, compre más :)
        """)
        system("pause")
        system("cls")