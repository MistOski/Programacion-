# A) Crear un diccionario que contenga como claves el código postal de cada ciudad. Cada 
#clave debe tener como valor un sub-diccionario con la siguiente información: "Ciudad", 
#"Temperatura" y "Precipitación". Luego imprimir el diccionario. (20 Pts)
diccionarioca = {
    "5700000" : {
        "ciudad" : "castro",
        "temperatura" : 11.8,
        "precipitacion" : 2000
    }    
}   

diccionarioch = {
    "5770000" : {
        "ciudad" : "chonchi",
        "temperatura" : 8.3,
        "precipitacion" : 2800
    }    
}   

diccionarioqu = {
    "5790000" : {
        "ciudad" : "quellon",
        "temperatura" : 10.2,
        "precipitacion" : 2950
    }    
}   
print("A.")
print(f"Castro: {diccionarioca}")
print(f"Chonchi: {diccionarioch}")
print(f"Quellon: {diccionarioqu}")

#C) Agregar al sub-diccionario de Castro una nueva clave "Meses Más Lluviosos" que 
#contenga una lista vacía. Luego, utilizar el método correspondiente de Python, para 
#agregar los tres meses uno a uno en cada ciudad. Los meses a agregar son: Mayo, Junio, Julio. (10 Pts) 
 #También se solicita eliminar el segundo mes “Junio” utilizando otro método de Python.  
castroactualizado = diccionarioca = {
    "5700000" : {
        "ciudad" : "castro",
        "temperatura" : 11.8,
        "precipitacion" : 2000,
    }    
}   

diccionarioch = diccionarioch = {
    "5770000" : {
        "ciudad" : "chonchi",
        "temperatura" : 8.3,
        "precipitacion" : 2800
    }    
}   

#D) Actualizar el valor de "Ciudad" para la ciudad de Chonchi, cambiándolo por "Ciudad de 
#los Tres Pisos" utilizando el método adecuado de Python. (10 Pts)
print("D.")
chonchiactualizado2 = diccionarioch = {
    "5770000" : {
        "Ciudad de los tres pisos" : "chonchi",
        "temperatura" : 8.3,
        "precipitacion" : 2800
    }    
}   
print(diccionarioch)

#E) Crear una lista llamada “lluvias” que contenga la precipitación de las tres ciudades. Luego: (20 Pts) 
#● Mostrar la suma total de precipitaciones utilizando el método correcto de Python. 
#● Mostrar la mayor y menor precipitación, utilizando los métodos correctos. 
#● Mostrar el índice (posición) de la precipitación más alta utilizando el método  correspondiente. 
print("E.")
lluvias = [2000, 2800, 2950]
suma = sum(lluvias)
may = max(lluvias)
men = min(lluvias)
print(f"La suma de todas las precipitaciones es: {suma}, la mayor precipitacion es: {may}, la menor precipitacion es: {men}")

#G) Obtener una lista de tuplas con las claves y valores del diccionario utilizando el método correspondiente. (15 Pts) 
print("G.")
castrotupla = castroactualizado.values()
tuplacastro = tuple(castrotupla)
listacastro = list(tuplacastro)
chonchitupla = chonchiactualizado2.values()
tuplachonchi = tuple(chonchitupla)
listachonchi = list(tuplachonchi)
quellontupla = diccionarioqu.values()
tuplaquellon = tuple(quellontupla)
listaquellon = list(tuplaquellon)
print(listacastro)
print(listachonchi)
print(listaquellon)