# 8) Modificar el nombre según la opción (mayúscula, minúscula, capitalizado)
nombre = input("Ingrese su nombre: ")
opcion = input("Ingrese una opcion (1-Mayusculas, 2-Minusculas, 3-Con primera mayuscula): ")

if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())
else:
    print("Opcion invalida.")