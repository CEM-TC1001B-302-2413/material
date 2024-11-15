import random

def crear_tablero():
    # [0, 1, 2, 3, 4, 5, 6, 7, 8]
    tablero = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    return tablero

def mostrar_tablero(tablero):
    print(f"""Tablero actual:
 {tablero[0]} | {tablero[1]} | {tablero[2]} 
-----------
 {tablero[3]} | {tablero[4]} | {tablero[5]} 
-----------
 {tablero[6]} | {tablero[7]} | {tablero[8]}""")
    
def juego_terminado(tablero):
    # horizontales
    if tablero[0] != " " and tablero[0] == tablero[1] and tablero[0] == tablero[2]:
        return True, tablero[0]
    elif tablero[3] != " " and tablero[3] == tablero[4] and tablero[3] == tablero[5]:
        return True, tablero[3]
    elif tablero[6] != " " and tablero[6] == tablero[7] and tablero[6] == tablero[8]:
        return True, tablero[6]
    # verticales
    elif tablero[0] != " " and tablero[0] == tablero[3] and tablero[0] == tablero[6]:
        return True, tablero[0]
    elif tablero[1] != " " and tablero[1] == tablero[4] and tablero[1] == tablero[7]:
        return True, tablero[1]
    elif tablero[2] != " " and tablero[2] == tablero[5] and tablero[2] == tablero[8]:
        return True, tablero[2]
    # diagonales
    elif tablero[0] != " " and tablero[0] == tablero[4] and tablero[0] == tablero[8]:
        return True, tablero[0]
    elif tablero[6] != " " and tablero[6] == tablero[4] and tablero[6] == tablero[2]:
        return True, tablero[6]
    for casilla in tablero:
        if casilla == " ":
            return False, ""
    return True, "Gato"
    
def juego():
    figura_jugador = "o"
    figura_máquina = "x"
    # turno jugador -> 1, turno máquina -> 2
    turno = random.randint(1,2)
    tablero = crear_tablero()
    terminado, ganador = juego_terminado(tablero)
    print("Las casillas están numeradas del 1 al 9.")
    print(f"Tu figura es: {figura_jugador}")
    print(f"La figura de la máquina es: {figura_máquina}")
    while not terminado:
        mostrar_tablero(tablero)
        if turno == 1: # Jugador
            print("Es tu turno.")
            tirada_jugador = int(input("Ingresa el número de la casilla donde quieres tirar: "))
            while tirada_jugador < 1 or tirada_jugador > 9 or tablero[tirada_jugador-1] != " ":
                print("Debes elegir una casilla que exista y que esté vacia.")
                tirada_jugador = int(input("Ingresa el número de la casilla donde quieres tirar: "))
            tablero[tirada_jugador-1] = figura_jugador
            turno = 2
        else: # Máquina
            print("Turno de la máquina.")
            casillas_vacías = []
            for casilla in range(len(tablero)):
                if tablero[casilla] == " ":
                    casillas_vacías.append(casilla)
            tirada_máquina = random.choice(casillas_vacías)
            tablero[tirada_máquina] = figura_máquina
            turno = 1
        terminado, ganador = juego_terminado(tablero)
    mostrar_tablero(tablero)
    if ganador == figura_jugador:
        print("Felicidades, has ganado la partida.")
    elif ganador == figura_máquina:
        print("Más suerte para la próxima, la máquina te ha vencido.")
    else:
        print("Gato.")

juego()