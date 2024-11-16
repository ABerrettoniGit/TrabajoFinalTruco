import random
from time import sleep

from clases.jugador import Jugador
from clases.carta import Carta

def crear_mazo():
        valores = ["1", "2", "3", "4", "5", "6", "7", "10", "11", "12"]
        palos = ["espada", "basto", "oro", "copa"]

        mazo = [Carta(valor, palo) for palo in palos for valor in valores]
        random.shuffle(mazo)

        return mazo
    
def valor_carta(carta) -> int:
    # Diccionario de jerarquía de cartas

    jerarquia = {
        ("1", "espada"): 14,
        ("1", "basto"): 13,
        ("7", "espada"): 12,
        ("7", "oro"): 11,
        ("3", None): 10,
        ("2", None): 9,
        ("1", None): 8,
        ("12", None): 7,
        ("11", None): 6,
        ("10", None): 5,
        ("7", None): 4,
        ("6", None): 3,
        ("5", None): 2,
        ("4", None): 1,
    }

    # Clave específica (valor y palo)
    clave_especifica = (carta.valor, carta.palo)
    # Clave general (valor sin importar palo)
    clave_general = (carta.valor, None)

    # Retorna el valor según la jerarquía, o un valor por defecto si no se encuentra
    return jerarquia.get(clave_especifica, jerarquia.get(clave_general, 0))
        
    


def comparar_cartas(carta1, carta2):
    valor1 = valor_carta(carta1)
    valor2 = valor_carta(carta2)

    print(f"DEBUG: {carta1} tiene valor {valor1}, {carta2} tiene valor {valor2}")

    if valor1 > valor2:
        print(f"{carta1} gana la ronda.")
        return carta1  
    elif valor2 > valor1:
        print(f"{carta2} gana la ronda.")
        return carta2  
    else:
        print("Empate.")
        return None  
    
def mostrar_estado(jugador1, jugador2):
    print(f"\nPuntos {jugador1.nombre}: {jugador1.puntos} | Puntos {jugador2.nombre}: {jugador2.puntos}")
    print("")
    print(f"{jugador1.nombre} mano: {jugador1.mostrar_mano()}")
    print(f"{jugador2.nombre} mano: secreto")

def jugar_truco(nombre_jugador: str):
    mazo = crear_mazo()
    jugador1 = Jugador(nombre_jugador)
    jugador2 = Jugador("Jugador 2")

    jugador1.recibir_cartas(mazo[0:3])
    jugador2.recibir_cartas(mazo[3:6])

    print(jugador1.mostrar_mano())

    numero_carta_max = 3

    for ronda in range(3):
        print(f"\n--- Ronda {ronda + 1} ---")
            
        
        if numero_carta_max > 1: 

            seleccion_carta = int(input(f"Ingrese la carta que quiere jugar: (1 , {numero_carta_max}) "))
            while seleccion_carta > len(jugador1.mano) :
                seleccion_carta = int(input(f"Ingrese un numero entre 1 y {numero_carta_max}: "))

            numero_carta_max -= 1

            carta1 = jugador1.mano.pop(seleccion_carta - 1)

            print(". . .")
            sleep(1)
        else:
            print("RONDA AUTOMATICA")
            sleep(3)
            carta1 = jugador1.mano.pop(0)
        
        
        carta2 = jugador2.mano.pop(0)

        print(f"{jugador1.nombre} juega: {carta1}")
        print("")
        print(f"{jugador2.nombre} juega: {carta2}")
        print(" ")
        ganador = comparar_cartas(carta1, carta2)
        
        if ganador == carta1:
            print(f"{jugador1.nombre} gana esta ronda!")
            jugador1.ganar_punto()
        elif ganador == carta2:
            print(f"{jugador2.nombre} gana esta ronda!")
            jugador2.ganar_punto()
        else:
            print("Empate esta ronda.")

        mostrar_estado(jugador1, jugador2)
       
    if jugador1.puntos > jugador2.puntos:
        print(f"\n¡El Ganador es {jugador1.nombre}!")
    elif jugador2.puntos > jugador1.puntos:
        print("\n¡El Ganador es Jugador 2!")
    else:
        print("\n¡Es un empate!")
    



