def desarmar_cadena(cadena, indice=0):
    if indice == len(cadena): 
       return
    else:
       print(cadena[indice]) # Imprime el carácter actual
       desarmar_cadena(cadena, indice + 1)

cadena = str(input("Ingrese una palabra o frase: "))
desarmar_cadena(cadena)
