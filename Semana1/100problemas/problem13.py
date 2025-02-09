def celsius_a_fahrenheit(c): return (c * 9/5) + 32
def celsius_a_kelvin(c): return c + 273.15
def fahrenheit_a_celsius(f): return (f - 32) * 5/9
def fahrenheit_a_kelvin(f): return (f - 32) * 5/9 + 273.15
def kelvin_a_celsius(k): return k - 273.15
def kelvin_a_fahrenheit(k): return (k - 273.15) * 9/5 + 32


valor = float(input("Ingrese la temperatura: "))
de = input("Desde (C, F, K): ").upper()
a = input("Hacia (C, F, K): ").upper()

conversiones = {
    ("C", "F"): celsius_a_fahrenheit,
    ("C", "K"): celsius_a_kelvin,
    ("F", "C"): fahrenheit_a_celsius,
    ("F", "K"): fahrenheit_a_kelvin,
    ("K", "C"): kelvin_a_celsius,
    ("K", "F"): kelvin_a_fahrenheit
}

resultado = conversiones.get((de, a), lambda x: "Conversión no válida")(valor)

print(f"Resultado: {resultado}")