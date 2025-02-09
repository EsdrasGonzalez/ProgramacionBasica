lista = [5, 2, 8, 4, 9, 1, 3, 6]

def ordenar_burbuja(lista):

    for i in range(len(lista)):

        for j in range(len(lista)-1):

            if lista[j] > lista[j+1]:

                lista[j], lista[j+1] = lista[j+1], lista[j]

ordenar_burbuja(lista) 

print(lista)





def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[len(lista) // 2]
    izquierda = [x for x in lista if x < pivote]
    medio = [x for x in lista if x == pivote]
    derecha = [x for x in lista if x > pivote]
    return quick_sort(izquierda) + medio + quick_sort(derecha)

print(quick_sort([5, 3, 8, 1, 2])) 







lista = [5, 3, 8, 1, 2]
lista.sort()  
print(lista) 

lista = sorted([5, 3, 8, 1, 2]) 
print(lista)  

