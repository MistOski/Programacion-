#CONDICIONAL IF 
edad = 19
if edad >= 18 and edad < 65:  #Se agrego el "and" para asegurarse de que este cumpla las dos condiciones para segurar el primer print
      print("Eres mayor de edad")
elif edad >= 65:
      print("Eres un adulto mayor") #"elif" es una tercera opcion que permite extender la funcion de "if"
else:
      print("Eres menor de edad") #Se finaliza la funcion con "else", y se llega a la ultima condicion (es el SiNo de python)


#USO DEL COLORAMA
from colorama import init, Fore
init()
print(Fore.MAGENTA + "UTILIZANDO IF Y ELSE")

#TRUE Y FALSE CON IF 
licencia = False
edad = 19 
automovil = False

if licencia:
      print("Tiene licencia de conducir")
else:
      print("No tiene licencia de conducir")
print("Este print esta fuera de alcance") #No esta dentro del "if"

if licencia and edad >= 18:
      print("Puedo conducir por que soy mayor de edad y tengo licencia")
elif automovil: 
      print("Tengo licencia, pero no automovil")
else: 
      print("No puedo conducir por que no tengo la edad, la licencia y el automovil")