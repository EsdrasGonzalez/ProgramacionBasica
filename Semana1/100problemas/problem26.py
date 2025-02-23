# Convertir n´ umeros de Decimales a Hexadecimal
numero = int(input("Ingresa un número decimal: "))


hexadecimal = hex(numero)[2:].upper()  
print("Hexadecimal:", hexadecimal)