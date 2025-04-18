#Función que imprime la tabla de multiplicar de un número del 1 al 10
def tabla_multiplicar(numero):
    print(f"\nTabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

#Programa principal

numero = int(input("Ingresá un número para ver su tabla de multiplicar: "))
tabla_multiplicar(numero)