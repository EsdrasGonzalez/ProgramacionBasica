
def ubicadorDeVocales(cadena):
    # Diccionario para almacenar las vocales y sus ubicaciones, ahora incluyendo mayúsculas
    vocales = 'aeiouáéíóúAEIOUÁÉÍÓÚ'
    ubicaciones = {v: [] for v in vocales}
    
    # Recorrer cada carácter de la cadena
    for i, char in enumerate(cadena):
        if char in vocales:  # Verificar si es una vocal (minúscula o mayúscula)
            ubicaciones[char].append(i)
    
    # Eliminar las vocales que no fueron encontradas
    ubicaciones = {v: ubicaciones[v] for v in ubicaciones if ubicaciones[v]}
    
    return ubicaciones

# Realizar las pruebas de escritorio
print(ubicadorDeVocales("murcielago"))
print(ubicadorDeVocales("eucalipto"))
print(ubicadorDeVocales("Albericoque"))





