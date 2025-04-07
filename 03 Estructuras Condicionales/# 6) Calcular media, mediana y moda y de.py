# 6) Calcular media, mediana y moda y determinar el sesgo
import random
from statistics import mean, median, mode

numeros_aleatorios = [random.randint(1, 100) for i in range (50)]

media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)