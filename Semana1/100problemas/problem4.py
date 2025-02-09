def fibonacci_iterativo(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

num = int(input("Ingresa el número de términos: "))
fibonacci_iterativo(num)