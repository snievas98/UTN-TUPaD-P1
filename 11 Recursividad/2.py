def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def mostrar_fibonacci(hasta):
    for i in range(hasta + 1):
        print(f"F({i}) = {fibonacci(i)}")

# Ejemplo:
mostrar_fibonacci(6)
# Salida: F(0) = 0, F(1) = 1, ..., F(6) = 8