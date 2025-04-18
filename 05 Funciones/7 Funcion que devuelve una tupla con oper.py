#Función que devuelve una tupla con operaciones básicas
def operaciones_basicas(a, b):
    if b == 0:
        division = "No se puede dividir por cero"
    else:
        division = a/b
    return a+b, a-b, a*b, division

#Programa principal

a = int(input("Ingresá el primer número: "))
b = int(input("Ingresá el segundo número: "))

suma, resta, multiplicacion, division = operaciones_basicas(a,b)

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")