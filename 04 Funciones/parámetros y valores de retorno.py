# Definición de una función sin parámetros y sin valor de retorno
def suma1():
    x = float(input("Ingresa el valor de x: "))
    y = float(input("Ingresa el valor de y: "))
    resultado = x + y
    print(f"El resultado de la suma es: {resultado}")
# suma1()

# Definición de una función con parámetros y sin valor de retorno
def suma2(x, y):
    resultado = x + y
    print(f"El resultado de la suma es: {resultado}")
    
#suma2(5,7)
#a = float(input("Ingresa x:"))
#b = float(input("Ingresa y:"))
#suma2(a,b)
#suma2("hola", "mundo")
    
def suma3(x, y):
    resultado = x + y
    return resultado

res = suma3(3,5)
print(res)
    
    
    
    