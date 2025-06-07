"""
Ejercicio 7 - Operaciones con sets de estudiantes aprobados
"""

parcial1 = {1, 2, 3, 4, 5}
parcial2 = {4, 5, 6, 7}

# Estudiantes que aprobaron ambos parciales
print("Aprobaron ambos:", parcial1 & parcial2)

# Estudiantes que aprobaron solo uno de los dos
print("Solo uno:", parcial1 ^ parcial2)

# Estudiantes que aprobaron al menos uno
print("Al menos uno:", parcial1 | parcial2)