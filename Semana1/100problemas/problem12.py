

a = int(input("Ingresa un número: "))
b = int(input("Ingresa un número: "))
c = int(input("Ingresa un número: "))

if a != b and a != c and b != c:  
    if a > b and a > c:
        print("El número mayor es: ",a)
    elif b > c:
        print("El número mayor es: ",b)
    else:
        print("El número mayor es: ",c)
else:
    print("Ingresa tres números diferentes")



