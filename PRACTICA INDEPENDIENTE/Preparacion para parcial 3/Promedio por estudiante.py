# Lista de notas
notas = [
    [6.0, 5.5, 6.3],  # Alumno 1
    [4.2, 5.0, 5.8],  # Alumno 2
    [7.0, 6.8, 6.9]   # Alumno 3
]

# Contador para saber qué alumno estamos viendo
alumno_num = 1

# Recorremos cada fila (alumno)
for alumno in notas:
    nota1 = alumno[0]
    nota2 = alumno[1]
    nota3 = alumno[2]
    
    promedio = (nota1 + nota2 + nota3) / 3
    
    print("Alumno", alumno_num, "tiene promedio", round(promedio, 2))
    
    alumno_num += 1
    
