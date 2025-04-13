num = int(input("Ingresar un número entero positivo:"))

if num < 0:
    print("Tiene que ser un número positivo")
else:
    sum = 0
    for i in range(0, num + 1): # El +1 se usa para incluir el valor final (num), que no se cuenta en el range.
        sum += i
    print("La suma total desde 0 hasta", num, "es:", sum)