#Convertir numeros de Decimales a Octal
numero = int(input("Ingresa un número decimal: "))

octal = oct(numero)[2:]  

print("Octal:", octal)