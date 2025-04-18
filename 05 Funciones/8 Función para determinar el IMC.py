#Función para determinar el IMC
def calcular_imc(peso, altura):
    return (peso / altura ** 2)

#Programa principal

peso=float(input("Ingresá tu peso en kilogramos: "))
altura=float(input("Ingresá tu altura expresada en metros:  "))
IndiceMC = calcular_imc(peso, altura)

print(f"Tu IMC es: {IndiceMC:.2f}")

if IndiceMC < 18.50:
    print ("Tenes un peso bajo, Te recomiendo que vayas al nutricionista")
elif IndiceMC > 18.50 or IndiceMC < 24.00:
    print ("Estás en un peso normal, felicitaciones!")
elif IndiceMC >= 25:
    print ("Tenes sobrepeso, te recomiendo que vayas al nutricionista")
elif IndiceMC >= 30:
    print ("Tenes obesidad, te recomiendo que vayas al nutricionista")