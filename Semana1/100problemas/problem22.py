#Calcular el area y volumen de distintas figuras geometricas.
import math

def calcular_area_volumen(figura, *dimensiones):
    if figura == "cuadrado":
        return dimensiones[0] ** 2
    elif figura == "rectangulo":
        return dimensiones[0] * dimensiones[1]
    elif figura == "triangulo":
        return (dimensiones[0] * dimensiones[1]) / 2
    elif figura == "trapecio":
        return ((dimensiones[0] + dimensiones[1]) * dimensiones[2]) / 2
    elif figura == "circulo":
        return math.pi * dimensiones[0] ** 2
    elif figura == "cubo":
        return dimensiones[0] ** 3
    elif figura == "prisma":
        return dimensiones[0] * dimensiones[1] * dimensiones[2]
    elif figura == "esfera":
        return (4/3) * math.pi * dimensiones[0] ** 3
    elif figura == "cilindro":
        radio, altura = dimensiones
        area_total = 2 * math.pi * radio * (radio + altura)
        volumen = math.pi * radio ** 2 * altura
        return area_total, volumen
    elif figura == "cono":
        radio, altura = dimensiones
        generatriz = math.sqrt(radio**2 + altura**2)
        area_total = math.pi * radio * (radio + generatriz)
        volumen = (1/3) * math.pi * radio ** 2 * altura
        return area_total, volumen
    else:
        return "Figura no reconocida"

if __name__ == "__main__":
    figura = input("Ingrese el nombre de la figura geométrica: ").strip().lower()
    dimensiones = list(map(float, input("Ingrese las dimensiones separadas por espacio: ").split()))
    resultado = calcular_area_volumen(figura, *dimensiones)
    print("Resultado:", resultado)


