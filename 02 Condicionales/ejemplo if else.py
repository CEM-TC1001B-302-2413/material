edad = int(input("Ingresa tu edad: "))
padrón = input("¿Estás inscrito en el padrón electoral? Sí/No: ").strip().lower()
if edad >= 18 and (padrón == "sí" or padrón == "si"):
    print("Eres mayor de edad.")
    print("Y además, puedes votar.")
else:
    print("Todavía no puedes votar.")