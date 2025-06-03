#Crear un algoritmo que sirva de Conversor de Temperatura: 

#Solicitar por consola una temperatura en grados Celsius (números flotantes)
c = float(input("Ingresa un numero: "))

#Calcular su equivalente en grados Fahrenheit y Kelvin utilizando las fórmulas correspondientes.

#Formula de Celcius a Farenheit = (0 °C × 9/5) + 32
f = (c * 9/5) + 32

#Formula de Celcius a Kelvin = 0 °C + 273.15
k = c + 273.15

#Mostrar los tres valores en pantalla, redondeados a 2 decimales.
print(f"La temperatura de grados Celcius ingresada es de: {c: .2f}, en grados Farenheit es de: {f: .2f} y en grados Kelvin es de: {k: .2f}")