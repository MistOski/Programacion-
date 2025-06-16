#Registrar nombre y 3 notas de un estudiante (0.0 a 7.0). Validar entradas, calcular promedio, categorizar:
#Bajo (<4.0), Regular (4.0–6.0), Alto (>6.0). Si >5.0, mostrar “(Becado)”.
nombre = input("Ingresa el nombre del estudiante: ")
notas = []

for i in range(3):
    while True:
        try:
            nota = float(input(f"Ingrese nota {i+1} (0.0 a 7.0): "))
            if 0.0 <= nota <= 7.0:
                notas.append(nota)
                break
            else:
                print("Nota fuera de rango.")
        except ValueError:
            print("Formato incorrecto.")

promedio = sum(notas) / 3

if promedio < 4.0:
    rendimiento = "Bajo"
elif promedio <= 6.0:
    rendimiento = "Regular"
else:
    rendimiento = "Alto"

beca = "(Becado)" if promedio > 5.0 else ""

print(f"{nombre} tiene promedio {promedio:.2f}, rendimiento: {rendimiento} {beca}")

# Evalúa bucles, manejo de errores, listas, cálculos y operadores ternarios.