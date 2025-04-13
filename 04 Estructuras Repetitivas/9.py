totalnumeros = 100
suma = 0

for i in range(totalnumeros):
    num = int(input(f"Ingrese un numero {i+1}: "))
    suma += num

media = suma / totalnumeros

print("La media de los", totalnumeros, "números ingresados es:", media)