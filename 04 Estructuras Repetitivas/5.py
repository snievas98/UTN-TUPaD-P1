import random #Importar la librería para generar números aleatorios

num_random = random.randint (0,9) 
intentos = 0

print("Adivina el número secreto entre 0 y 9!")

num_usuario = -1 #Colocar un valor distinto al random para que entre al bucle

while num_usuario != num_random:
    num_usuario = int(input("Escribe un numero:"))
    intentos += 1

print ("¡Correcto! Lo lograste en", intentos, "intentos.")