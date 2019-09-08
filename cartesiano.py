import math
xa = float (input("Insira o primeiro número:"))
ya = float (input("Insira o segundo número:"))
xb = float (input("Insira o terceiro número:"))
yb = float (input("Insira o quarto número:"))

distancia = math.sqrt ((xa - xb) **2 + (ya - yb) **2)

if distancia >= 10:
    print("longe")
else:
    print("perto")