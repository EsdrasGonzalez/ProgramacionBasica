def interes_compuesto(capital, tasa, tiempo):
    monto = capital * (1 + tasa) ** tiempo
    interes = monto - capital
    return monto, interes

# Entrada de datos
C = float(input("Ingresa el capital inicial: "))
r = float(input("Ingresa la tasa de interés (en porcentaje, sin el %): ")) / 100
t = float(input("Ingresa el tiempo en años: "))

# Cálculo
monto_final, interes_ganado = interes_compuesto(C, r, t)

# Salida de resultados
print(f"\nMonto final: {monto_final:.2f}")
print(f"Interés ganado: {interes_ganado:.2f}")