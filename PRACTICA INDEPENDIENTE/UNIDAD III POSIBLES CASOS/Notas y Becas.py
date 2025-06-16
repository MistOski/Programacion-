#Solicita 3 notas de un estudiante (de 0.0 a 7.0). Calcula su promedio y entrega:
#Categoría: Bajo (<4.0), Regular (4.0–6.0), Alto (>6.0)
#Si tiene beca (promedio >5.0)
notas = []
for i in range(3):
    while True:
        try:
            nota = float(input(f"Ingrese nota {i+1}: "))
            if 0.0 <= nota <= 7.0:
                notas.append(nota)
                break
            else:
                print("La nota debe estar entre 0.0 y 7.0")
        except ValueError:
            print("Formato inválido. Usa punto decimal.")

promedio = sum(notas) / 3

if promedio < 4.0:
    categoria = "Bajo"
elif promedio <= 6.0:
    categoria = "Regular"
else:
    categoria = "Alto"

beca = " (Becado)" if promedio > 5.0 else ""

print(f"Promedio: {promedio:.2f} - Categoría: {categoria}{beca}")

# El programa usa validaciones anidadas, condicionales, listas y cálculo promedio.
# También muestra uso de operador ternario para "Becado".