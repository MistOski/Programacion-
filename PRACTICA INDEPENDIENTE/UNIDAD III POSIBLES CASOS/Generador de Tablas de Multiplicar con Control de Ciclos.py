num = int(input("Ingresa un número entre 1 y 9: "))

for i in range(1, 11):
    resultado = num * i
    if resultado > 50:
        print(f"{num} x {i} = {resultado} (Límite alcanzado)")
        break
    print(f"{num} x {i} = {resultado}")
else:
    print("Tabla generada correctamente.")

# Evalúa bucle for, break y uso de else al final del for.