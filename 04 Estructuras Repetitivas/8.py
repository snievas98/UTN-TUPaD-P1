pares = 0
impares = 0
positivos = 0
negativos = 0

totalnumeros = 100

for i in range(totalnumeros):
    num = int(input(f"Ingrese un numero {i+1}: "))

    # Contar pares e impares
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

    # Contar positivos y negativos
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
    # Los ceros no se cuentan como positivos ni negativos

# Mostrar resultados
print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)
print("Cantidad de números positivos:", positivos)
print("Cantidad de números negativos:", negativos)