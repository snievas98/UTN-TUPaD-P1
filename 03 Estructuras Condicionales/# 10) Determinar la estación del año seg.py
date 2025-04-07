# 10) Determinar la estación del año según fecha y hemisferio
hemisferio = input("Ingrese su hemisferio (N/S): ").upper()
mes = int(input("Ingrese el numero del mes (1 a 12): "))
dia = int(input("Ingrese el dia del mes: "))

fecha = (mes, dia)

if (fecha >= (12, 21) or fecha <= (3, 20)):
    estacion_norte = "Invierno"
    estacion_sur = "Verano"
elif (fecha >= (3, 21) and fecha <= (6, 20)):
    estacion_norte = "Primavera"
    estacion_sur = "Otoño"
elif (fecha >= (6, 21) and fecha <= (9, 20)):
    estacion_norte = "Verano"
    estacion_sur = "Invierno"
elif (fecha >= (9, 21) and fecha <= (12, 20)):
    estacion_norte = "Otoño"
    estacion_sur = "Primavera"
else:
    print("Fecha invalida")
    exit()

if hemisferio == "N":
    print("Estas en:", estacion_norte)
elif hemisferio == "S":
    print("Estas en:", estacion_sur)
else:
    print("Hemisferio invalido")