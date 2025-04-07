# 7) Ver si una palabra termina en vocal y agregar "!"
texto = input("Ingrese una palabra o frase: ")

if texto[-1].lower() in "aeiou":
    texto += "!"

print(texto)