#USO DE MATCH
print("MENU")
print("1. Hamburguesa")
print("2. Pizza")
print("3. Completo")

opcion = input("Por favor, elige una opcion (1-3): ")

match opcion:
    case "1":
        print("Eligio una hamburguesa") #El match es parecido a la funcion "if", pero permite mas alternativas
    case "2":
        print("Eligio la pizza")
    case "3":
        print("Eligio el completo")
    case _: 
        print ("No eligio nada, para que vino...") #EL "case_:" es equivalente a un else

mes = 10
match mes:
    case 12 | 1 | 2:
        print("Verano")
    case 3 | 4 | 5:
        print("Otoño")
    case 6 | 7 | 8:
        print("Invierno")    
    case 9 | 10 | 11:
        print("Primavera")
    case _:
        print("Mes invalido")

#VALORES COMPUESTOS
x = [1, 2, 3]
match x:
    case [a, b, c]: #DESAGRUPANDO VALORES DE LA LISTA X 
        print(f"Elementos de la lista x: {a}, {b}, {c}")

#MATCH CON DICCIONARIO
datos = {
    "nombre": "victor",
    "edad": 31,
}
match datos:
    case {"nombre": n, "edad": e}:
        print(f"Nombre: {n}, Edad: {e}")
