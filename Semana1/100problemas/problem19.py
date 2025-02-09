import random

n = int(input("Cantidad de números aleatorios: "))

print("Uniforme (0-1):", [random.uniform(0, 1) for _ in range(n)])
print("Enteros (1-1000000000):", [random.randint(1, 1000000000) for _ in range(n)])
