#Función con parametros nombre, apellido, edad y residencia

def informacion_personal(nombre, apellido, edad, residencia):
    mensaje = f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia} "
    print(mensaje)

#Programa principal

nombre = input("Ingresá tu nombre: ")
apellido = input("Ingresá tu apellido: ")
edad = input("Ingresá tu edad: ")
residencia = input("Ingresá tu residencia: ")

informacion_personal(nombre, apellido, edad, residencia)