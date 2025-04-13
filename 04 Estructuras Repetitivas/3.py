num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))

#Esta condición es para que el orden de los numeros enteros ingresados no afecte el resultado.
# Si el primer número es mayor que el segundo, se intercambian.
# Esto permite recorrer correctamente los valores intermedios en el bucle.

if num1 > num2:
    num1, num2 = num2, num1

suma = 0
for i in range(num1 + 1, num2):
    suma += i

print("La suma es:",suma)