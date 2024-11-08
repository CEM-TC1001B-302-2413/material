lista = ["Uriel", "Karime", "Daniela", "Riccardo", "Daniel", "Luis", "Giovanni", "Jorge"]
nombre = input("Ingresa el nombre del alumno a buscar: ")
encontrado = False
for i in lista:
    if i == nombre:
        encontrado = True
if encontrado == True:
    print(f"{nombre} está en la lista.")
else:
    print(f"{nombre} no está en la lista.")
# --------------------------------------------

for i in lista:
    if i == nombre:
        print(f"{nombre} está en la lista.")
        break # Detiene la ejecución del ciclo
        # continue -> Detiene la iteración actual y se pasa a la siguiente
else: # Se ejecuta si el ciclo no se detuvo con un break
    print(f"{nombre} no está en la lista.")
