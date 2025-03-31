agenda = []

def agregar_contacto():
    nombre = input("Nombre: ")
    numero = input("Número: ")
    correo = input("Correo: ")
    agenda.append((nombre, numero, correo))

def buscar_contacto():
    nombre = input("Nombre del contacto a buscar: ")
    for contacto in agenda:
        if contacto[0] == nombre:
            print(contacto)
            return
    print("No encontrado")

def listar_contactos():
    for contacto in sorted(agenda):
        print(contacto)

while True:
    opcion = input("\n1. Agregar\n2. Buscar\n3. Listar\n4. Salir\nOpción: ")
    if opcion == "1": agregar_contacto()
    elif opcion == "2": buscar_contacto()
    elif opcion == "3": listar_contactos()
    elif opcion == "4": break

