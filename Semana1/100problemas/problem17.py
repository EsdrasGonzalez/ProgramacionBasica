#Crear un conversor de unidades.

def convertir(valor, de, a):
    conversiones = {
        "m_km": 0.001, "km_m": 1000,
        "cm_m": 0.01, "m_cm": 100,
        "kg_g": 1000, "g_kg": 0.001,
        "lb_kg": 0.453592, "kg_lb": 2.20462
    }
    
    return valor * conversiones.get(f"{de}_{a}", "Conversión no disponible")

valor = float(input("Ingrese el valor: "))
de = input("Unidad de origen (m, km, cm, kg, g, lb): ")
a = input("Unidad de destino (m, km, cm, kg, g, lb): ")

resultado = convertir(valor, de, a)
print("Resultado:", resultado)


