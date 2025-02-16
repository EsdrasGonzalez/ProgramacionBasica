def contar_vocales_consonantes(texto):
    texto = texto.lower()  
    vocales = "aeiouáéíóú"
    
    num_vocales = sum(1 for letra in texto if letra in vocales)
    num_consonantes = sum(1 for letra in texto if letra.isalpha() and letra not in vocales)

    print(f"Vocales: {num_vocales}, Consonantes: {num_consonantes}")
texto = input("Ingrese una cadena: ")
contar_vocales_consonantes(texto)


