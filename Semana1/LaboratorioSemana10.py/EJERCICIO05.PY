
def km_a_millas(km):
    return km * 0.621371

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def litros_a_galones(litros):
    return litros * 0.264172


def main():
    while True:
        print("\nElige una opción de conversión:")
        print("1. Kilómetros a Millas")
        print("2. Celsius a Fahrenheit")
        print("3. Litros a Galones")
        print("4. Salir")
        
        opcion = input("Selecciona una opción (1/2/3/4): ")
        
        if opcion == "1":
            km = float(input("Ingresa la cantidad en kilómetros: "))
            print(f"{km} kilómetros son {km_a_millas(km)} millas.")
        
        elif opcion == "2":
            celsius = float(input("Ingresa la temperatura en Celsius: "))
            print(f"{celsius}°C son {celsius_a_fahrenheit(celsius)}°F.")
        
        elif opcion == "3":
            litros = float(input("Ingresa la cantidad en litros: "))
            print(f"{litros} litros son {litros_a_galones(litros)} galones.")
        
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        
        else:
            print("Opción no válida. Por favor, elige una opción válida.")

if __name__ == "__main__":
    main()
