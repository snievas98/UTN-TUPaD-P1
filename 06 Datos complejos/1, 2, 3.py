"""
Ejercicios 1, 2 y 3 - Gestión de precios de frutas
"""

# Ejercicio 1: Diccionario inicial y añadir frutas nuevas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# Ejercicio 2: Actualizar precios
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

# Ejercicio 3: Crear lista de frutas (sin precios)
lista_frutas = list(precios_frutas.keys())
print("Frutas disponibles:", lista_frutas)