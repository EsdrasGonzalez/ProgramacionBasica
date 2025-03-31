import random


def generar_lista(n):
    return [random.randint(1, 1000) for _ in range(n)]


def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[0]
    menores = [x for x in lista[1:] if x <= pivote]
    mayores = [x for x in lista[1:] if x > pivote]
    return quicksort(menores) + [pivote] + quicksort(mayores)


def busqueda_binaria(lista, objetivo):
    bajo = 0
    alto = len(lista) - 1
    while bajo <= alto:
        medio = (bajo + alto) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            bajo = medio + 1
        else:
            alto = medio - 1
    return -1 

def main():
    
    n = int(input("Ingresa la cantidad de números en la lista: "))
    
    lista = generar_lista(n)
    
    print("\nLista original:")
    print(lista)
    
    lista_ordenada = quicksort(lista)
    
    
    print("\nLista ordenada:")
    print(lista_ordenada)
    
  
    objetivo = int(input("\nIngresa el número que deseas buscar: "))
    
   
    resultado = busqueda_binaria(lista_ordenada, objetivo)
    
    
    if resultado != -1:
        print(f"\nEl número {objetivo} fue encontrado en el índice {resultado}.")
    else:
        print(f"\nEl número {objetivo} no fue encontrado en la lista.")


main()
