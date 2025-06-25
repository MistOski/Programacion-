diccionario = {
    "Hola" : {"ll": 33, "MM" : 33},
    "Eu" : {"EO" : "L", "LO": 44}, #Diccionario
    "A" : {"P" : "A", "PA" : 2}
}
diccionario["Hola"]["ll"] = 44 #Actualizar diccionario

primeraclave = list(diccionario.keys())[0]  #Se pasa el diccionario a lista para usar el pop

diccionario.pop(primeraclave) #Se elimina lo primero de la lista

print(diccionario)

frutas = ["frutilla", "pera", "manzana"]
precios = [100, 200, 300]

print(
    dict(
        zip(frutas, precios) #Junta de listas a diccionario
    )
)

alumnos = {
    "alumno1" : {"nota1" : 2.9, "nota2" : 6.0},
    "alumno2" : {"nota1" : 5.4, "nota2" : 3.4},
    "alumno3" : {"nota1" : 4.0, "nota2" : 4.1}
}

for nombre, notas in alumnos.items():
    total = 0
    cantidadnotas = 0
    for nota in notas.values():
        total += nota
        cantidadnotas += 1
    
    promedio = total / cantidadnotas

if promedio > 4.0:
    