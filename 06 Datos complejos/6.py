"""
Ejercicio 6 - Cálculo de promedios con tuplas
"""

alumnos = {}

# Ingresar 3 alumnos y sus notas
for _ in range(3):
    nombre = input("Nombre del alumno: ")
    notas = tuple(float(input(f"Ingresá nota {i+1} de {nombre}: ")) for i in range(3))
    alumnos[nombre] = notas

# Mostrar promedios
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre} - Promedio: {promedio:.2f}")