# Implementar una calculadora con historial de operaciones.
import math

historial = []

def calcular(op, a=None, b=None):
    ops = {
        "1": (a + b, f"{a} + {b} = {a + b}"),
        "2": (a - b, f"{a} - {b} = {a - b}"),
        "3": (a * b, f"{a} × {b} = {a * b}"),
        "4": (a / b if b != 0 else "Error: División por 0", f"{a} ÷ {b} = {a / b}" if b != 0 else "Error"),
        "5": (a ** b, f"{a} ^ {b} = {a ** b}"),
        "6": (math.sqrt(a) if a >= 0 else "Error", f"√{a} = {math.sqrt(a)}" if a >= 0 else "Error")
    }
    return ops[op]

while True:
    op = input("\n1.Sumar 2.Restar 3.Multiplicar 4.Dividir 5.Potencia 6.Raíz 7.Historial 8.Salir\nOpción: ")
    
    if op == "8":
        break
    elif op == "7":
        print("\n".join(historial) if historial else "Historial vacío.")
    else:
        a = float(input("Número: "))
        b = float(input("Segundo número: ")) if op in "12345" else None
        resultado, operacion = calcular(op, a, b)
        historial.append(operacion)
        print("Resultado:", resultado)
