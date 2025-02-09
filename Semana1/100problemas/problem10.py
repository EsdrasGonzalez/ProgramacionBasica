
with open("archivo.txt", "w") as archivo:
    archivo.write("Hola, este es un archivo de texto.\n")


with open("archivo.txt", "r") as archivo:
    print("Contenido actual:")
    print(archivo.read())


with open("archivo.txt", "a") as archivo:
    archivo.write("Nueva línea agregada.\n")


with open("archivo.txt", "r") as archivo:
    lineas = archivo.readlines()

lineas = [line.replace("Hola", "Hola, mundo") for line in lineas]

with open("archivo.txt", "w") as archivo:
    archivo.writelines(lineas)


with open("archivo.txt", "r") as archivo:
    print("\nContenido después de modificar:")
    print(archivo.read())