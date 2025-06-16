#Pide al usuario una lista de números separados por coma. El programa debe:
#Convertir los valores a enteros (usando map() y split()).
#Clasificar cada número como par, impar o primo (usando for-else).
#Guardar los resultados en un diccionario: clave = número, valor = tipo.
#Mostrar cuántos hay de cada tipo usando count().
entrada = input("Ingresa números separados por coma: ")
numeros = list(map(int, entrada.split(",")))
clasificacion = {}

for num in numeros:
    if num % 2 == 0:
        tipo = "Par"
    else:
        # Verificar si es primo
        for i in range(2, num):
            if num % i == 0:
                tipo = "Impar"
                break
        else:
            tipo = "Primo"
    clasificacion[num] = tipo

# Contar
tipos = list(clasificacion.values())
print("Clasificación por número:")
for num, tipo in clasificacion.items():
    print(f"{num} → {tipo}")

print("\nResumen:")
print(f"Pares: {tipos.count('Par')}")
print(f"Impares: {tipos.count('Impar')}")
print(f"Primos: {tipos.count('Primo')}")