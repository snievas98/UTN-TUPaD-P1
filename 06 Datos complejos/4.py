"""
Ejercicio 4 - Agenda telefónica simple
"""

agenda = {}

# Cargar 5 contactos
for _ in range(5):
    nombre = input("Nombre del contacto: ")
    telefono = input("Número de teléfono: ")
    agenda[nombre] = telefono

# Consultar un contacto
consulta = input("¿A quién querés buscar? ")
if consulta in agenda:
    print(f"Número de {consulta}: {agenda[consulta]}")
else:
    print("Contacto no encontrado.")