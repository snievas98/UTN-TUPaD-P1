#Funcion que devuelve un saludo

def saludar_usuario(nombre):
    return f"Hola {nombre}!"

#Programa principal

nombre_usuario = input("Ingresá tu nombre: ")
saludo = saludar_usuario(nombre_usuario)
print(saludo)