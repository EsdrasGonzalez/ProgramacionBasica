
class Vehiculo:
    def __init__(self, marca, modelo, anio, precio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.precio = precio
    
    def mostrar_informacion(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.anio}")
        print(f"Precio: ${self.precio}")

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, anio, precio, numero_puertas):
        super().__init__(marca, modelo, anio, precio)
        self.numero_puertas = numero_puertas
    
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Número de puertas: {self.numero_puertas}")


class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, anio, precio, cilindrada):
        super().__init__(marca, modelo, anio, precio)
        self.cilindrada = cilindrada
    
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Cilindrada: {self.cilindrada} cc")

def obtener_datos_automovil():
    marca = input("Ingresa la marca del automóvil: ")
    modelo = input("Ingresa el modelo del automóvil: ")
    anio = int(input("Ingresa el año del automóvil: "))
    precio = float(input("Ingresa el precio del automóvil: "))
    numero_puertas = int(input("Ingresa el número de puertas del automóvil: "))
    return Automovil(marca, modelo, anio, precio, numero_puertas)

def obtener_datos_motocicleta():
    marca = input("Ingresa la marca de la motocicleta: ")
    modelo = input("Ingresa el modelo de la motocicleta: ")
    anio = int(input("Ingresa el año de la motocicleta: "))
    precio = float(input("Ingresa el precio de la motocicleta: "))
    cilindrada = int(input("Ingresa la cilindrada de la motocicleta (en cc): "))
    return Motocicleta(marca, modelo, anio, precio, cilindrada)

automovil = obtener_datos_automovil()
motocicleta = obtener_datos_motocicleta()

print("\nInformación del automóvil:")
automovil.mostrar_informacion()

print("\nInformación de la motocicleta:")
motocicleta.mostrar_informacion()



