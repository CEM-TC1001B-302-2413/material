# FizzBuzz
# Ingresar un número
# Si el número es divisible entre 3 -> Fizz
# Si el número es divisible entre 5 -> Buzz
# Si el número es divisible entre 3 y entre 5 -> FizzBuzz
# Si el número no es divisible ni entre 3 ni entre 5 -> número
número = int(input("Ingresa el número a revisar: "))
if número % 3 == 0 and número % 5 == 0:
    print("FizzBuzz")
elif número % 3 == 0:
    print("Fizz")
elif número % 5 == 0:
    print("Buzz")
else:
    print(número)