while True:
    try:
        numero = int(input("Ingresa un número entero positivo: "))
        if numero > 0:
            break
        else:
            print("Debe ser mayor que cero.")
    except ValueError:
        print("Entrada inválida. Debes ingresar un número entero.")

print("Número válido ingresado:", numero)

# Se usa try-except para evitar errores al convertir a int.
# El while True se usa como bucle hasta que se cumpla la condición de entrada válida.
# Ejercicio típico para evaluar manejo de excepciones.