productos = {
    "Smartphone": 300,
    "Laptop": 800,
    "Tablet": 150,
    "Smartwatch": 200
}

for nombre, precio in productos.items():
    if precio < 200:
        categoria = "Económico"
    elif 200 <= precio <= 500:
        categoria = "Estándar"
    else:
        categoria = "Premium"
    
    print(f"{nombre}: ${precio} → {categoria}")
    
# Se recorren los productos con un bucle for.
# Se aplica condicional múltiple con if-elif-else.
# Ideal para evaluar comprensión de diccionarios, bucles y condicionales.