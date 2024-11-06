# Juego de piedra, papel o tijeras
# Vamos a pedir que el usuario ingrese su opción
# Vamos a hacer que la máquina elija aleatoriamente su opción
# Determinar el ganador y mostrar el resultado
import random
print("Bienvenido al juego de piedra, papel o tijeras")
tirada_jugador = int(input("Ingresa 1) Piedra, 2) Papel, 3) Tijeras: "))
if tirada_jugador >= 1 and tirada_jugador <= 3:
    tirada_máquina = random.randint(1,3)
    print(f"La máquina tiró: {tirada_máquina}")
    if tirada_jugador == tirada_máquina:
        print("El juego fue un empate.")
    elif tirada_jugador == 1 and tirada_máquina == 2 or \
         tirada_jugador == 2 and tirada_máquina == 3 or \
         tirada_jugador == 3 and tirada_máquina == 1:
        print("La máquina ha ganado")
    else:
        print("Has ganado la partida")
else:
    print("Debes elegir entre 1) Piedra, 2) Papel y 3) Tijeras")