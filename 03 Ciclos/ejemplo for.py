# Ciclor for

# range(5) -> 0,1,2,3,4
# range(final)
for i in range(5):
    print(f"El valor de i es: {i}")
    
print("-"*30)

# range(5,10) -> 5,6,7,8,9
# range(inicio, final)
for i in range(5,10):
    print(f"El valor de i es: {i}")
    
print("-"*30)

# range(5,20,3) -> 5,8,11,14,17
# range(inicio, final, paso)
for i in range(5,20,3):
    print(f"El valor de i es: {i}")
    
print("-"*30)

for i in range(20,5,-3):
    print(f"El valor de i es: {i}")
    
print("-"*30)

texto = "Hola mundo"

for i in texto:
    print(f"El valor de i es: {i}")

print("-"*30)

lista = [2, 6.4, "Hola", True, [1,2,3], "Adiós"]

for i in lista:
    print(f"El valor de i es: {i}")

print("-"*30)

texto = "Hola mundo, ¿cómo estás?"
lista = texto.split()
print(lista)
for i in lista:
    print(f"Palabra: {i}")











