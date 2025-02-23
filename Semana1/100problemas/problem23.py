# Calcular la mediana y la moda de una lista de numeros.
import statistics

numeros = list(map(int, input("Ingresa los números separados por espacios: ").split()))

mediana = statistics.median(numeros)
moda = statistics.mode(numeros)

print("Mediana:", mediana)
print("Moda:", moda)
