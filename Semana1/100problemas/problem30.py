#Determinar si un numero es primo y generar los primos menores a  el.
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def primos_menores(n):
    return [x for x in range(2, n) if es_primo(x)]


num = int(input("Ingresa un número: "))


if es_primo(num):
    print(f"{num} es primo.")
else:
    print(f"{num} no es primo.")

print("Primos menores:", primos_menores(num))

