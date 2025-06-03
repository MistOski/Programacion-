#Crear un algoritmo que permita manipular cadenas de texto:

#Ingresar una frase de máximo 30 caracteres.    
f = (input("Ingrese una frase, el maximo es de 30 caracteres, aquellos que superen el limite no seran considerados: "))
f = f[:30] #No se establece un limite directamente, solo se limita la cantidad de caracteres a considerar dentro de la frase 

#Generar dos nuevas variables: una en mayúsculas y otra en minúsculas. 
ma = f.lower() 
mi = f.upper() #Se establecen las minusculas y mayusculas, luego se imprimen
print (f"Frase en mayusculas: {ma}")
print (f"Frase en minusculas: {mi}")

#Utilizar un método propio para determinar cuántas veces aparece la letra «a» (tanto «a» como «A») en la frase, y muestra el total.
ca = f.count("a")
cA = f.count("A") 
s = ca + cA #Se crean 2 variables que cuentan el caracter asignado, acto seguido se suman e imprimen
print(f"La cantidad de caracteres A es de {s}, se consideran mayusculas y minusculas")

#Emplear otro método para imprimir la longitud de la frase original. 
l = len(f) #Se usa el "len" para calcular la cantidad de caracteres
print(f"La cantidad de caracteres dentro de la frase es de {l}, los espacios tambien son considerados.")