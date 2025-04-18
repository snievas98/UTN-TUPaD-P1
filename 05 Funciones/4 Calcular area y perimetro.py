import math #Importamos la librería de matematica

#Funciones para calcular radio

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

#Programa principal

R = float(input("Ingresá el área del círculo: "))

area = calcular_area_circulo(R)
perimetro = calcular_perimetro_circulo(R)

print(f"Área del círculo: {area:.2f}")
print(f"Perímetro del círculo: {perimetro:.2f}")