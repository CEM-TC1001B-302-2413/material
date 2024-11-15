import turtle as t
import random

def figura_regular(largo_lado, numero_lados):
    for i in range(numero_lados):
        t.forward(largo_lado)
        t.right(360/numero_lados)
figuras = random.randint(5,30)
for i in range(figuras):
    figura_regular(random.randint(100,200), random.randint(3, 8))
t.mainloop()
