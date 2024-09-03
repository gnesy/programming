
nombre = 'a'

while(nombre != nombre.upper()):
    
    nombre = input("Ingrese su nombre en mayusculas: ")
    
    if(nombre == nombre.upper()):
        if(nombre[0] == 'A'):
            print(nombre.lower())
        else: 
            break
    else: 
        print("El nombre dbee estar en MAYUSCULAS!!!")
    
    



