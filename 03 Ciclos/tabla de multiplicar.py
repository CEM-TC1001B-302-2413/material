número = int(input("Ingresa tu número: "))
# resuelto con for
for i in range(1, 11):
    resultado = i * número
    print(f"{número} x {i} = {resultado}")
# resuelto con while
i = 1
while i <= 10:
    resultado = i * número
    print(f"{número} x {i} = {resultado}")
    i += 1
