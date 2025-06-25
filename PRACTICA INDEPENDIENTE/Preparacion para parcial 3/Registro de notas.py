# Diccionario con subdiccionarios: nombre del alumno -> notas
alumnos = {
    "Camila": {"nota1": 5.5, "nota2": 6.0, "nota3": 4.8},
    "Luis":   {"nota1": 3.5, "nota2": 4.0, "nota3": 2.8},
    "Antonia":{"nota1": 6.5, "nota2": 6.0, "nota3": 6.2}
}

# Recorremos el diccionario
for nombre, notas in alumnos.items():
    total = 0
    cantidad_notas = 0
    
    # Recorremos las notas del subdiccionario
    for nota in notas.values():
        total += nota
        cantidad_notas += 1
    
    promedio = total / cantidad_notas

    if promedio >= 4.0:
        estado = "Aprobado"
    else:
        estado = "Reprobado"
    
    print(f"{nombre}: Promedio = {promedio:.2f} = {estado}")

