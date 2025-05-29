#GUIA DE TIPOS DE DATOS DE PYTHON

#INICIALIZANDO VARIABLES NUMERICAS
edad = 31
estatura = 17.7
peso = 75
complejo = 1 + 4j
complejo02 = complex(1, 4)
print(complejo)
print(complejo02)

#OPERACION ARITMETICA
imc = peso / (estatura ** 2) #El "**" sirve para elevar un numero
print(f"Su IMC es: {imc}")

#FORMATO DE SALIDA DEL RESULTADO (UTILIZANDO F-STRINGS Y : .2f
print(f"Su IMC es: {imc: .4f}") #Salida con 2 decimales

#TRANSFORMANDO UN NUMERO ENTERO EN UN NUMERO FLOTANTE
print(float(edad))

#REDODEANDO EL RESULTADO CON EL "round"
print(round(imc))

#DATOS DE TIPO DE STRING (CADENAS DE TEXTO)
carrera = "Ingenieria civil en informatica"
asignatura = "Programacion"
descripcion = '''Esta asignatura del primer semestre'''

#IMPRESION DE CARACTERES EN UNA CADENA DE TEXTO
print(carrera[0]) #El 0 nos da la primera letra del texto, los espacios igual cuentan como "algo" por lo que de haber un espacio apareceria vacio
print(carrera[-1]) #Los numeros negativos nos imprimen los caracteres al revez

#PRUEBA DE FLEXIBILIDAD DE PYTHON
print ("Hola" * 4) #Se pueden multiplicar los textos (Particularidad de Python)
#print ("Hola"/2) Aunque no se puede con la division

#UTILIZANDO EL INTERVALO DE UNA CADENA 
print(asignatura[0:5]) #Se generan solo los primeros 5 caracteres (Los indicados en el codigo)

#USO DE "split" (GENERA UN ARREGLO DE CADENAS)
print(descripcion.split()) #Separo los textos

#ARREGLO NUMERICO 
v = [1, 2, 3, 4, 5] #Inicializando un arreglo numerico (Solo apareceran los que se asignen)
print(v[0])

#FUNCION LEN
print(f'La carrera {carrera} tiene:', len(carrera), 'caracteres')

#VALORES BOLEANOS 
interruptor = True
ampolleta = False #Los boleanos son el verdadero y falso
print(interruptor, ampolleta)

#FUNCION TYPE
print(type(interruptor)) #Permite saber el tipo de dato que se utiliza 

#COMPARATIVA DE VALORES LOGICOS 
print(1<10)
print(100<=20) #Si los numeros son iguales o mayores dependiendo lo que se especifique se mostrara como verdadero o falso
print(100==100)
print(bool(""))
print(bool(1)) #El 0 y el vacio "", son tomados como falso al no ser considerados "algo"
print(bool(0))