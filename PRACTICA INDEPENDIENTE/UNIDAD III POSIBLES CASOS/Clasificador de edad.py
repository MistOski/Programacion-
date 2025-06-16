edad = int(input("Ingresa tu edad: "))

if edad < 18:
    print("Eres menor de edad")
elif edad >= 65:
    print("Eres adulto mayor")
else:
    print("Eres adulto")
    
# Se usa if-elif-else para cubrir tres rangos de edad.
# El elif es más eficiente que múltiples if, ya que las condiciones son mutuamente excluyentes.