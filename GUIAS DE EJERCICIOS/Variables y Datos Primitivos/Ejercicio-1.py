#Crear un algoritmo que sirva de Conversor de Temperatura: 

#Solicitar por consola una temperatura en grados Celsius (números flotantes)
c = float(input("Ingrese un valor la cual sera considerado en temperaturas Celcius, este valor sera pasado a grados Farenheit y Kelvin: "))


#Calcular su equivalente en grados Fahrenheit y Kelvin utilizando las fórmulas correspondientes.
#Formula de Celcius a Farenheit = (0 °C × 9/5) + 32
f = (c * 9/5) + 32

#Formula de Celcius a Kelvin = 0 °C + 273.15
k = c + 273.15 

#Mostrar los tres valores en pantalla, redondeados a 2 decimales.
print(f"Su valor de {round(c, 2)} grados Celcius es equivalente a {round(f, 2)} grados Farenheit, y {round(k, 2)} grados Kelvin")