#Conversión de Distancias

#Todos los resultados deben mostrarse con 2 decimales. Solicita una distancia en kilómetros y muestra:
km = int(input("Ingresa un numero para calcular la distancia en kilometros, la cantidad que ingreses sera considerada en kilometros: "))

#Su valor en metros (1 km = 1000 m)
m = km * 1000 
 
#Su valor en millas (1 km ≈ 0.621371)
mi = km * 0.621371

print(f"El valor ingresado es de {m: .2f} metros y de {mi: .2f} en millas")