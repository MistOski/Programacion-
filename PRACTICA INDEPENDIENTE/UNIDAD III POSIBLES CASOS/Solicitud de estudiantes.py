# Solicitud de cantidad de estudiantes
while True:
    try:
        cantidad = int(input("¿Cuántos estudiantes desea registrar?: "))
        if cantidad > 0:
            break
        else:
            print("Debe ingresar un número entero mayor que 0.")
    except ValueError:
        print("Entrada inválida. Ingrese un número entero.")

# Registro del nombre de la asignatura
asignatura = input("Ingrese el nombre de la asignatura: ")

# Diccionario para almacenar datos de estudiantes
estudiantes = {}

# Registro de datos de cada estudiante
for i in range(cantidad):
    print(f"\nEstudiante {i+1}")
    nombre = input("Nombre del estudiante: ")
    notas = []

    for j in range(3):
        while True:
            try:
                nota = float(input(f"Ingrese nota {j+1} (0.0 a 7.0): "))
                if 0.0 <= nota <= 7.0:
                    notas.append(nota)
                    break
                else:
                    print("La nota debe estar entre 0.0 y 7.0.")
            except ValueError:
                print("Formato inválido. Use punto decimal si es necesario.")
    
    estudiantes[nombre] = tuple(notas)

# Cálculo de promedios y clasificación
promedios = {}
for nombre, notas in estudiantes.items():
    promedio = sum(notas) / 3
    promedios[nombre] = promedio

# Máximo y mínimo
max_estudiante = max(promedios, key=promedios.get)
min_estudiante = min(promedios, key=promedios.get)

print("\n=== Resultados Académicos ===")
print(f"\nEstudiante con mejor promedio: {max_estudiante} ({promedios[max_estudiante]:.2f})")
print(f"Estudiante con peor promedio: {min_estudiante} ({promedios[min_estudiante]:.2f})")

# Categorías y beca
print("\nClasificación por estudiante:")
for nombre, promedio in promedios.items():
    if promedio < 4.0:
        categoria = "Bajo"
    elif promedio <= 6.0:
        categoria = "Regular"
    else:
        categoria = "Alto"
    
    becado = " (Becado)" if promedio > 5.0 else ""
    print(f"{nombre}: Promedio={promedio:.2f} → Rendimiento {categoria}{becado}")

# Reprobados
print("\nEstudiantes reprobados (promedio < 4.0):")
for nombre, promedio in promedios.items():
    if promedio < 4.0:
        print(f"- {nombre}: {promedio:.2f}")