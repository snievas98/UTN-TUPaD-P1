"""
Ejercicio 5 - Análisis de frase: palabras únicas y frecuencia
"""

frase = input("Escribí una frase: ")
palabras = frase.lower().split()

# Palabras únicas
unicas = set(palabras)
print("Palabras únicas:", unicas)

# Frecuencia de palabras
frecuencias = {}
for palabra in palabras:
    frecuencias[palabra] = frecuencias.get(palabra, 0) + 1

print("Frecuencia de palabras:", frecuencias)