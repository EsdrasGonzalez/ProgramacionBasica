import math

a = float(input("Ingrese a: "))
b = float(input("Ingrese b: "))
c = float(input("Ingrese c: "))

d = b**2 - 4*a*c  

if d < 0:
    print("No tiene soluciones reales")
elif d == 0:
    print("Solución única:", -b / (2 * a))
else:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print("Soluciones:", x1, "y", x2)