import random
seguir_jugando = 1
while seguir_jugando == 1:
    intentos = 1
    número_aleatorio = random.randint(1,100)
    número_elegido = int(input("Ingresa un número entre 1 y 100: "))
    while número_elegido != número_aleatorio:
        if número_elegido < número_aleatorio:
            print("El número que buscas es mayor al que ingresaste.")
        else:
            print("El número que buscas es menor al que ingresaste.")
        número_elegido = int(input("Ingresa un número entre 1 y 100: "))
        intentos += 1
    print(f"Adivinaste, te tomó {intentos} intentos.")
    seguir_jugando = int(input("¿Desea seguir jugando? 1)Sí, 2)No: "))
print("Hasta la próxima.")