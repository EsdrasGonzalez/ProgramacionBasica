def analizar_texto(texto):
    palabras = texto.lower().split()
    total_palabras = len(palabras)
    palabras_unicas = set(palabras)
    frecuencia_palabras = {}
    
    for palabra in palabras:
        if palabra in frecuencia_palabras:
            frecuencia_palabras[palabra] += 1
        else:
            frecuencia_palabras[palabra] = 1
    
    palabra_mas_frecuente = ""
    max_frecuencia = 0
    for palabra, frecuencia in frecuencia_palabras.items():
        if frecuencia > max_frecuencia:
            palabra_mas_frecuente = palabra
            max_frecuencia = frecuencia
    
    print("Número total de palabras:", total_palabras)
    print("Cantidad de palabras únicas:", len(palabras_unicas))
    print("Frecuencia de palabras:", frecuencia_palabras)
    print("Palabra más frecuente:", palabra_mas_frecuente, "(Aparece", max_frecuencia, "veces)")

texto = input("Ingrese un texto: ")
analizar_texto(texto)