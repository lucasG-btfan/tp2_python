#13- Pedir el ingreso de dos cadenas por por teclado, indicar si la segunda cadena se encuentra dentro de la primera.

cadena1 = input("Ingresa una texto: ")
cadena2 = input("Ingresa una palabra: ")
result = cadena1.find(cadena2)

if result == -1:
    print("La palabra no se encuentra dentro de la frase")
else:
    print("La palabra se ecuentra dentro de la frase")
