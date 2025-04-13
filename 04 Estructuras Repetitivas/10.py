# Solicitamos al usuario que ingrese un número entero
numero = int(input("Ingrese un número entero: "))

# Variable para ir construyendo el número invertido
invertido = 0

# Trabajamos con el valor absoluto para evitar errores con números negativos
num_original = abs(numero)

# Usamos un bucle while para extraer los dígitos y construir el número invertido
while num_original > 0:
    digito = num_original % 10             # Extraemos el último dígito (resto de dividir por 10)
    invertido = invertido * 10 + digito    # Lo agregamos al invertido, desplazando los anteriores
    num_original //= 10                    # Eliminamos el último dígito dividiendo por 10 (entero)

# Si el número original era negativo, le damos el mismo signo al resultado
if numero < 0:
    invertido *= -1

print("Número invertido:", invertido)