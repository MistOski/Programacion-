n = int(input("Ingresa un número mayor a 1: "))

if n <= 1:
    print("Debe ser mayor que 1")
else:
    for i in range(2, n):
        if n % i == 0:
            print(f"{n} no es primo (divisible por {i})")
            break
    else:
        print(f"{n} es primo")

# El else del for solo se ejecuta si el for NO se interrumpe con break.
# Ejercicio excelente para evaluar comprensión de for-else.