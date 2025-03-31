
def mergesort(lista):
    if len(lista) > 1:
        medio = len(lista) // 2  
        izquierda = lista[:medio]   
        derecha = lista[medio:]  

        mergesort(izquierda)  
        mergesort(derecha)  

        i = j = k = 0

       
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1

      
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        
        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1


n = int(input("Cuántos números deseas ingresar: "))
lista = []

for i in range(n):
    numero = int(input(f"Ingresa el número {i + 1}: "))
    lista.append(numero)


print("\nLista antes de ordenar:")
print(lista)


mergesort(lista)

print("\nLista después de ordenar:")
print(lista)
