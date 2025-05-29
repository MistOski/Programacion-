estudiantes = ('Samir', 'Matias','Hector', 'Pia', 'Carlos')

#USO DE SORTED
print(sorted(estudiantes)) #Sorted puede usarse en las tuplas a diferencia de sort, la cual tambien cambia la tupla por una lista

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

#FUNCION APPEND
ramos.append('Habilidades comunicativas')
print(ramos)

#FUNCION INSERT
ramos.insert(1, 'Algebra') #El numero indica la posicion donde se quiera agregar el elemento
print(ramos)

#FUNCION POP
ramos.pop() #Elimina lo ultimo de la lista 
print(ramos)

#FUNCION SORT 
ramos.sort(key=len) #Con key se agrega el len para ordenarlo por cantidad de caracteres, el key es una propiedad de la funcion sort
print(ramos)

#FUNCION EXTEND
ramos2 = ['Calculos, Automatas']
ramos.extend(ramos2) #Extendiendo una lista con otra 
print(ramos)