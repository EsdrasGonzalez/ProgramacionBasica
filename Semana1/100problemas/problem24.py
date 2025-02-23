# Encontrar el mınimo comun multiplo (MCM) de multiples numeros
import math
from functools import reduce

def mcm_multiple(nums):
    return reduce(math.lcm, nums)

numeros = list(map(int, input("Ingresa los números separados por espacios: ").split()))
print("MCM:", mcm_multiple(numeros))
