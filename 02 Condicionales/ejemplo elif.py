calificación = int(input("Ingresa tu calificación numérica: "))
if calificación >= 90 and calificación <= 100:
    print("A")
else:
    if calificación >= 80 and calificación <= 89:
        print("B")
    else:
        if calificación >= 70 and calificación <= 79:
            print("C")
        else:
            if calificación >= 60 and calificación <= 69:
                print("D")
            else:
                if calificación >= 0 and calificación <= 59:
                    print("F")
                    
# -----------------------------------------------------

if calificación >= 90 and calificación <= 100:
    print("A")
elif calificación >= 80 and calificación <= 89:
    print("B")
elif calificación >= 70 and calificación <= 79:
    print("C")
elif calificación >= 60 and calificación <= 69:
    print("D")
elif calificación >= 0 and calificación <= 59:
    print("F")
else:
    print("Debes ingresar una calificación entre 0 y 100")