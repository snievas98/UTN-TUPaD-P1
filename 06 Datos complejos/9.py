"""
Ejercicio 9 - Agenda con claves como tuplas (día, hora)
"""

agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de Python"
}

dia = input("Día: ")
hora = input("Hora (HH:MM): ")

evento = agenda.get((dia.lower(), hora))
if evento:
    print("Actividad:", evento)
else:
    print("No hay actividad registrada en ese horario.")