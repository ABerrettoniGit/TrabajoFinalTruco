from funciones.complementarias import *
from funciones.logica_juego import *

jugar = True

print("Seleccione la opcion que desea realizar: ")
print("1- Jugar nuevo juego")
print("2- Salir del programa")

opcion = int(input("Ingrese una opcion: "))
while opcion <= 0 or opcion >= 3:
    opcion = int(input("Ingrese una opcion correcta: "))
        

while jugar == True:

    match opcion:
        case 1:

            nombre = input("Ingrese su nombre: ")
            print(f"Bienvenido/a {nombre}")

            jugar_truco(nombre)
        case 2: 
            jugar = False
            print("Que tenga buen dia")
            break

    respuesta = input("Desea jugar de nuevo?: si/no ").lower()
    while respuesta != "si" and respuesta != "no":
        respuesta = input("Ingrese una opcion correcta: si/no ").lower()

    if respuesta == "si":
        jugar = True
    else:
        opcion = 2
       
