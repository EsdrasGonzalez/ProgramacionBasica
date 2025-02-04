num = int(input("Ingresa un número: "))

if num % 2 == 0:
    print(f"{num} es par.")
else:
    print(f"{num} es impar.")

multiplo = int(input("Ingresa otro número para verificar si es múltiplo (o 0 para omitir): "))

if multiplo != 0:
    if num % multiplo == 0:
        print(f"{num} es múltiplo de {multiplo}.")
    else:
        print(f"{num} NO es múltiplo de {multiplo}.")