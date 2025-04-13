sum = 0
num = int(input("Ingrese un número entero(0 para terminar): "))

#Mientras que la variable "num" sea distinto a 0 luego podemos ir sumando los valores que ingrese el usuario para la variable "sum" con "sum += num".
#Luego se repite el bucle hasta que el usuario ingrese el 0 y finaliza realizando el print con la suma total.

while num != 0:
    sum += num
    num = int(input("Ingrese un número entero(0 para terminar): "))

print ("La suma total es:", sum)