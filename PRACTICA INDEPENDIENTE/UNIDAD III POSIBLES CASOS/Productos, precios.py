# Información de productos, precios, ofertas y stock
productos = {
    "Smartphone": 300,
    "Laptop": 800,
    "Tablet": 150,
    "Smartwatch": 200
}

ofertas = {"Laptop", "Smartwatch"}

stock = {
    "Smartphone": 25,
    "Notebook": 12,   # Error en el enunciado: debería ser "Laptop" para coincidir con precios
    "Tablet": 8,
    "Smartwatch": 4
}

# --- 1. Precio más caro y más barato ---
precio_mas_caro = max(productos, key=productos.get)
precio_mas_barato = min(productos, key=productos.get)

print("=== Artículo más caro y más barato ===")
print(f"Más caro: {precio_mas_caro} (${productos[precio_mas_caro]})")
print(f"Más barato: {precio_mas_barato} (${productos[precio_mas_barato]})")

# --- 2. Categoría de precio por producto ---
print("\n=== Categorías de precio ===")
for nombre, precio in productos.items():
    if precio < 200:
        categoria = "Económico"
    elif precio <= 500:
        categoria = "Estándar"
    else:
        categoria = "Premium"
    
    print(f"{nombre}: ${precio} → {categoria}")

# --- 3. Artículos con stock bajo ---
print("\n=== Artículos con stock bajo (< 10 unidades) ===")
for nombre, cantidad in stock.items():
    if cantidad < 10:
        print(f"{nombre}: {cantidad} unidades")
        