
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b


def saludar(nombre):
    return f"Hola, {nombre}!"


class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def mostrar_info(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}"


def programa_principal():

    print("Paradigma Imperativo:")
    x = int(input("Ingresa el primer número: "))
    y = int(input("Ingresa el segundo número: "))
    
    if x > y:
        print(f"{x} es mayor que {y}")
    else:
        print(f"{y} es mayor que {x}")
    
    for i in range(1, 6):
        print(f"Contando: {i}")


    print("\nParadigma Estructurado:")
    nombre = input("¿Cómo te llamas? ")
    saludo = saludar(nombre)
    print(saludo)


    print("\nParadigma Modular:")
    a = int(input("Ingresa el primer número para suma/resta: "))
    b = int(input("Ingresa el segundo número para suma/resta: "))
    print(f"La suma de {a} y {b} es: {suma(a, b)}")
    print(f"La resta de {a} y {b} es: {resta(a, b)}")

   
    print("\nParadigma Orientado a Objetos:")
    marca = input("Ingresa la marca del vehículo: ")
    modelo = input("Ingresa el modelo del vehículo: ")
    vehiculo = Vehiculo(marca, modelo)
    print(vehiculo.mostrar_info())


programa_principal()

