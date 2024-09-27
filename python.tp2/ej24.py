"""24- Crea un programa que lea una cadena de texto carácter por carácter usando recursión.
Ejemplo: Ingreso “UTN FRM Mza”
Salida: U
T
N
F
R
M
M
z
a"""


def desarmar_cadena(cadena, indice=0):
    if indice == len(cadena): 
       return
    else:
       print(cadena[indice]) # Imprime el carácter actual
       desarmar_cadena(cadena, indice + 1)

cadena = str(input("Ingrese una palabra o frase: "))
desarmar_cadena(cadena)
