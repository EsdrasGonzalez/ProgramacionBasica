pila = []

pila.append(1)  
pila.append(2)
print(pila.pop()) 









from collections import deque

cola = deque()

cola.append(1)  
cola.append(2)
print(cola.popleft())









class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

n1 = Nodo(1)
n2 = Nodo(2)
n1.siguiente = n2  # Conectar nodos

print(n1.dato, "->", n1.siguiente.dato) 
