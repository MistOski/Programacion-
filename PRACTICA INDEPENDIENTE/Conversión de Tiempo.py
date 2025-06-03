#Pide al usuario ingresar un tiempo en horas. Luego calcula:
h = int(input("Ingrese una cantidad de horas"))

#El número de minutos.
hm = h * 60 

#El número de segundos.
hs = hm * 60 

#Imprime los tres valores con 0 decimales.
print(f"Su hora ingresada es: {h}, en minutos es de: {hm} y en segundos es de: {hs}")