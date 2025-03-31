import math

def calculadora_estadistica(*args):
    n = len(args)
    promedio = sum(args) / n
    mediana = sorted(args)[n//2] if n % 2 != 0 else (sorted(args)[n//2 - 1] + sorted(args)[n//2]) / 2
    desviacion_estandar = math.sqrt(sum((x - promedio) ** 2 for x in args) / n)
    return promedio, mediana, desviacion_estandar


numeros = list(map(float, input("Introduce los números separados por espacio: ").split()))


promedio, mediana, desviacion_estandar = calculadora_estadistica(*numeros)


print(f"Promedio: {promedio}")
print(f"Mediana: {mediana}")
print(f"Desviación estándar: {desviacion_estandar}")
