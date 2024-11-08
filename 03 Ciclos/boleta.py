promedio = 0
número_udfs = int(input("¿Cuántas udf cursaste en el semestre?: "))
for i in range(1, número_udfs+1):
    udf = float(input(f"Ingresa la calificación de tu uf{i}: "))
    promedio = promedio + udf
promedio = promedio / número_udfs
print(f"El promedio fue {promedio:,.2f}.")
if promedio >= 90:
    print("Excelente semestre.")
elif promedio >= 80:
    print("Buen semestre.")
elif promedio >= 70:
    print("Al menos pasaste")
else:
    print("Debes estudiar más.")
    
