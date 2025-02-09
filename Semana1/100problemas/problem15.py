annio = int(input("ingresa un año: "))
if (annio % 4 == 0 and annio % 100 != 0) or annio % 400 == 0:
    print("El año ", annio, "es bisiesto")
else:
    print("El año ", annio, "no es bisiesto")
    