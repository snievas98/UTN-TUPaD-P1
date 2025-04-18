#Funcion para pasar de Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    return celsius * 1.8 + 32

#Programa principal

celsius = float(input("Ingresá la temperatura en celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)

print(f"\n{celsius}°C a fahrenheit es {fahrenheit:.2f}°F")