udf1 = float(input("Ingresa la calificación de tu uf1: "))
udf2 = float(input("Ingresa la calificación de tu uf2: "))
udf3 = float(input("Ingresa la calificación de tu uf3: "))
udf4 = float(input("Ingresa la calificación de tu uf4: "))
udf5 = float(input("Ingresa la calificación de tu uf5: "))
udf6 = float(input("Ingresa la calificación de tu uf6: "))
udf7 = float(input("Ingresa la calificación de tu uf7: "))
promedio = (udf1 + udf2 + udf3 + udf4 + udf5 + udf6 + udf7) / 7
# Maneras clásicas de imprimir nuestro resultado
print("El promedio fue", promedio, " Excelente")
print("El promedio fue " + str(promedio) + ". Excelente")
print("El promedio fue {0:,.2f}. Excelente".format(36475858.256543))
# {} -> El contenido se va a cambiar por el valor que representa
# : -> Vamos a usar un formato especial
# , -> Incluir el separador de miles
# .2 -> Redondear a dos decimales
# f -> Mostrar el resultado como un número float
# Manera actual: f-string
print(f"El promedio fue {promedio:,.2f}. Excelente")
