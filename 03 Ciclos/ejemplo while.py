# for i in range(5,20,3):

i = 5 # inicio
while i < 20: # condición de paro
    print(f"El valor de i es: {i}")
    #i = i + 3
    i += 3 # paso

print("-"*30)

# for i in texto:
# 0 -> H
# 1 -> o
# 2 -> l
# ...
# 8 -> d
# 9 -> 0
texto = "Hola mundo"
i = 0
while i < len(texto):
    print(f"texto[{i}] = {texto[i]}")
    i += 1

print("-"*30)

lista = [1, 9.5, True, "hola", [5,7,2], False]
# len(lista) -> 6 (número de elementos en la secuencia)
i = 0
while i < len(lista):
    print(f"lista[{i}] = {lista[i]}")
    i += 1

print("-"*30)

calificación = float(input("Ingresa tu calificación: "))
while calificación < 0 or calificación > 100:
    print("Error, la calificación tiene que estar entre 0 y 100.")
    calificación = float(input("Ingresa tu calificación: "))
