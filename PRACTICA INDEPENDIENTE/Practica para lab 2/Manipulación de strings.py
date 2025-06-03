#Pide una palabra y muestra:
p = input("Ingresa una palabra: ")

#Cuántos caracteres tiene
c = len(p)

#La palabra en mayúsculas
pmin = p.lower()

#La palabra en minúsculas
pmay = p.upper()

#El primer y último carácter
pc = p[0]
uc = p[-1]
print(f"La palabra es: {p}, tiene {c} caracteres, se entrega en minusculas: {pmay}, se entrega en minusculas: {pmin}, primer caracter: {pc}, ultimo caracter: {uc}")
