"""
Ejercicio 8 - Inventario de productos
"""

stock = {
    "pan": 20,
    "leche": 15,
    "huevos": 30
}

producto = input("Ingresá un producto para consultar o actualizar: ")

if producto in stock:
    agregar = int(input(f"Hay {stock[producto]} unidades. ¿Cuántas querés agregar?: "))
    stock[producto] += agregar
else:
    nuevo = int(input("Producto nuevo. ¿Cuántas unidades tiene?: "))
    stock[producto] = nuevo

print("Stock actualizado:", stock)