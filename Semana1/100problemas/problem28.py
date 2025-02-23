# Calcular el area y el perımetro de figuras geometricas basicas.
import math

def area_perimetro_cuadrado(lado):
    area = lado ** 2
    perimetro = 4 * lado
    return area, perimetro

def area_perimetro_rectangulo(base, altura):
    area = base * altura
    perimetro = 2 * (base + altura)
    return area, perimetro

def area_perimetro_circulo(radio):
    area = math.pi * radio ** 2
    perimetro = 2 * math.pi * radio
    return area, perimetro

def area_perimetro_triangulo(base, altura, lado1, lado2, lado3):
    area = (base * altura) / 2
    perimetro = lado1 + lado2 + lado3
    return area, perimetro

print("Elige una figura geométrica:")
print("1. Cuadrado")
print("2. Rectángulo")
print("3. Círculo")
print("4. Triángulo")

opcion = int(input("Opción: "))

if opcion == 1:
    lado = float(input("Ingresa el lado del cuadrado: "))
    area, perimetro = area_perimetro_cuadrado(lado)
elif opcion == 2:
    base = float(input("Ingresa la base del rectángulo: "))
    altura = float(input("Ingresa la altura del rectángulo: "))
    area, perimetro = area_perimetro_rectangulo(base, altura)
elif opcion == 3:
    radio = float(input("Ingresa el radio del círculo: "))
    area, perimetro = area_perimetro_circulo(radio)
elif opcion == 4:
    base = float(input("Ingresa la base del triángulo: "))
    altura = float(input("Ingresa la altura del triángulo: "))
    lado1 = float(input("Ingresa el primer lado del triángulo: "))
    lado2 = float(input("Ingresa el segundo lado del triángulo: "))
    lado3 = float(input("Ingresa el tercer lado del triángulo: "))
    area, perimetro = area_perimetro_triangulo(base, altura, lado1, lado2, lado3)
else:
    print("Opción no válida.")
    exit()

print(f"Área: {area:.2f}")
print(f"Perímetro: {perimetro:.2f}")