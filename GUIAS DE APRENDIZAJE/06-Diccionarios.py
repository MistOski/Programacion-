#CREANDO DICCIONARIOS 
paciente = {
    'Nombre' : 'Carlos',
    'Apellido' : 'Santana',
    'Edad' : '50',
    'Ciudad' : 'Quellon'
    }
print(paciente)
print(type(paciente)) #Se comprueba que es un diccionario

#METODO ALTERNATIVO CON "DICT"
medico = dict(
    Nombre = 'Samir',
    Apellido = 'Arana',
    Edad = '20',
    Especialidad = 'Neurologo'
)
print(medico)

#SE ESPECIFICA LO QUE SE QUIERE IMPRIMIR
print(medico['Nombre'])

#ELIMINANDO UNA CLAVE (METODO DEL)
del(paciente['Nombre']) 
print(paciente)
