#Funcion para calcular promedio
def calcular_promedio(a,b,c):
    return (a + b + c) / 3

#Programa principal

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))

promedio = calcular_promedio(num1,num2,num3)

print(f"Tu promedio es de {promedio:.2f}")