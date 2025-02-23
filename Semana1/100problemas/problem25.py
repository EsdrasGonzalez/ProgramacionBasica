#Generar una contrasena segura con requisitos de longitud y complejidad
import random
import string

def generar_contrasena(longitud, mayusculas=True, numeros=True, simbolos=True):
    caracteres = string.ascii_lowercase
    if mayusculas:
        caracteres += string.ascii_uppercase
    if numeros:
        caracteres += string.digits
    if simbolos:
        caracteres += string.punctuation
    
    if longitud < 4: 
        raise ValueError("La longitud debe ser al menos 4 para cumplir con la complejidad.")
    
    return ''.join(random.sample(caracteres, longitud))

longitud = int(input("Ingresa la longitud de la contraseña: "))
mayusculas = input("¿Incluir mayúsculas? (s/n): ").strip().lower() == 's'
numeros = input("¿Incluir números? (s/n): ").strip().lower() == 's'
simbolos = input("¿Incluir símbolos? (s/n): ").strip().lower() == 's'

contrasena = generar_contrasena(longitud, mayusculas, numeros, simbolos)
print("Contraseña generada:", contrasena)