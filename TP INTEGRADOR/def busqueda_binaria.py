def busqueda_binaria(lista, valor):
    inicio = 0
    fin = len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == valor:
            return medio
        elif lista[medio] < valor:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1

lista = [1, 2, 3, 4, 7, 9]
print("Búsqueda binaria:", busqueda_binaria(lista, 9))  # Output: 5