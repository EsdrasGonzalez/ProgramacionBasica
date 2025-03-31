inventario = []

def agregar_producto():
    inventario.append({
        "nombre": input("Nombre: "),
        "categoria": input("Categoría: "),
        "precio": float(input("Precio: ")),
        "cantidad": int(input("Cantidad: "))
    })

def eliminar_producto():
    nombre = input("Nombre del producto a eliminar: ")
    global inventario
    inventario = [p for p in inventario if p["nombre"] != nombre]

def buscar_producto():
    nombre = input("Nombre del producto a buscar: ")
    print(next((p for p in inventario if p["nombre"] == nombre), "No encontrado"))

def mostrar_productos_ordenados():
    for p in sorted(inventario, key=lambda x: x["precio"]):
        print(p)

while True:
    opcion = input("\n1. Agregar\n2. Eliminar\n3. Buscar\n4. Mostrar ordenados\n5. Salir\nOpción: ")
    if opcion == "1": agregar_producto()
    elif opcion == "2": eliminar_producto()
    elif opcion == "3": buscar_producto()
    elif opcion == "4": mostrar_productos_ordenados()
    elif opcion == "5": break
