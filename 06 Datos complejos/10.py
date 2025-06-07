"""
Ejercicio 10 - Invertir diccionario país -> capital a capital -> país
"""

paises = {
    "Argentina": "Buenos Aires",
    "Francia": "París",
    "Japón": "Tokio"
}

capitales = {capital: pais for pais, capital in paises.items()}
print(capitales)