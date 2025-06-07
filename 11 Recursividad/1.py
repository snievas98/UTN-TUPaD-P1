def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def mostrar_factoriales(hasta):
    for i in range(1, hasta + 1):
        print(f"{i}! = {factorial(i)}")

# Ejemplo:
mostrar_factoriales(5)
# Salida: 1! = 1 ... 5! = 120