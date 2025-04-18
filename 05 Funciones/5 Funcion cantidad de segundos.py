#Función cantidad de segundos

def segundos_a_horas(segundos):
    return segundos / 3600

#Programa principal

segundos = int(input("Ingresá la cantidad de segundos y te digo cuantas horas son: "))
horas = segundos_a_horas(segundos)

print(f"{segundos} segundos son {horas:.2f} horas.")