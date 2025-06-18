#LISTA
letras = ["a", "b", "c", "c", "c", "d", "e", "b", "k", "j", "l", "m"]
#CONTANDO 
contadorA = letras.count("a")
contadorB = letras.count("b")
contadorC = letras.count("c")
contadorD = letras.count("d")
contadorE = letras.count("e")
contadorK = letras.count("k")
contadorJ = letras.count("j")
contadorL = letras.count("l")
contadorM = letras.count("m")
print(f"Cantidad de A = {contadorA} B = {contadorB} C = {contadorC} D = {contadorD} E = {contadorE} K = {contadorK} J = {contadorJ} L = {contadorL} M = {contadorM}")
#LIMPIANDO DUPLICADOS 
sinduplicados = set(letras)
letrasinduplicados = list(sinduplicados)
print(letrasinduplicados)
#AGREGANDO LETRAS
agregando = []
P = letrasinduplicados.append("p")
print(letrasinduplicados)
#BORRANDO 
letrasinduplicados.remove("a")
letrasinduplicados.pop(0)
letrasinduplicados.pop()
print(letrasinduplicados)
letrasinduplicados.pop(1)
print(letrasinduplicados)
#SEPARANDO Y UNIENDO
texto = "-".join(sinduplicados)
print(texto)
enlista = str(texto)
print(enlista)
separado = enlista.split("-")
print(separado)