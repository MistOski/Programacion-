#Implementar un sistema de control de inventario con las siguientes características:
#Cada producto se guarda en un diccionario, con nombre como clave y una lista con su stock, 
#precio unitario y si está en oferta (True/False).
#El sistema debe mostrar un menú con:
#Agregar producto
#Actualizar stock
#Calcular valor total de inventario
#Mostrar productos en oferta
#Salir
inventario = {}

while True:
    print("\nMenú:")
    print("1. Agregar producto")
    print("2. Actualizar stock")
    print("3. Calcular valor total")
    print("4. Mostrar productos en oferta")
    print("5. Salir")
    
    opcion = input("Elige una opción: ")

    match opcion:
        case "1":
            nombre = input("Nombre del producto: ")
            stock = int(input("Stock: "))
            precio = float(input("Precio unitario: "))
            oferta = input("¿Está en oferta? (s/n): ").lower() == "s"
            inventario[nombre] = [stock, precio, oferta]
        case "2":
            nombre = input("Producto a actualizar: ")
            if nombre in inventario:
                nuevo_stock = int(input("Nuevo stock: "))
                inventario[nombre][0] = nuevo_stock
            else:
                print("Producto no encontrado.")
        case "3":
            total = 0
            for datos in inventario.values():
                total += datos[0] * datos[1]
            print(f"Valor total del inventario: ${total:.2f}")
        case "4":
            for nombre, datos in inventario.items():
                if datos[2]:
                    print(f"{nombre} está en oferta (Precio: ${datos[1]:.2f})")
        case "5":
            print("Saliendo del programa.")
            break
        case _:
            print("Opción inválida.")   