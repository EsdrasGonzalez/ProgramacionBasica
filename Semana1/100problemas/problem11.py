texto = input("Ingrese una cadena: ").replace(" ", "").lower()
print("Es un palíndromo" if texto == texto[::-1] else "No es un palíndromo")


