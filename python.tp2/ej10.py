"""10- Convertir una cadena a mayúsculas o minúsculas, daremos opción a que el usuario pida que se desea
hacer (convertir a mayúsculas o convertir a minúsculas) y mostrar el resultado por pantalla."""

text = input("Escribe una palabra... ")

choice = input("Ingresa 1 si quieres convertir a mayusculas o 2 para convertir a minusculas ")

if choice == "2":
    textMin = text.lower()
    print(textMin)
# Convertir  todo a minuscula

elif choice == "1":
# Convertir todo a mayuscula
    textMay = text.upper()
    print(textMay)
else: 
    print("Por favor ingrese un numero valido (1 o 2)")
    exit()

