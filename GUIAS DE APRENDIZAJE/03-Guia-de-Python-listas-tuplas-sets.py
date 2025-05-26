#GUIA DE PYTHON

#LISTA COMPUESTA DE DATOS
lista1 = ['Victor', 31, True]
print(lista1) 

#LISTA VACIA
frutas = []
print(type(frutas)) 
#LISTA COMPUESTA DE NUMEROS
n = [1,2,3,4,5]
print(n)

#LISTA COMPUESTA DE STRINGS
ramos = ['Programacion', 'Quimica', 'Matematicas']
print(ramos)

#IMPRIME LA POSICION DEL PRIMER ELEMENTO De LA LISTA (NO EL CARACTER)
print(ramos[0]) #Imprime lo primero de la lista

#FUNCION COUNT (CUENTA LA CANTIDAD DE OCURRENCIAS DE UN ELEMENTO)
print(ramos.count('Programacion'))

#CREANDO E INSTANCIANDO UNA TUPLA 
estudiantes = ('Samir', 'Matias', 'Hector')
print(type(estudiantes)) #Se verifica el tipo de dato (En este caso saldra tupla)

#FUNCION INDEX EN TUPLAS
print(estudiantes.index('Hector')) #Index indica la posicion (En este caso 0)

#CREANDO SETS
colores = {'Azul'. 'Rojo', 'Azul' 'Verde'}
print(colores)