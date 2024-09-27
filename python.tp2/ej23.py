cadena=input("diga una frase: ")
cantidad=len(cadena)
i=cantidad
conjunto = []
def reordenarcadena(i):
    conjunto.append(cadena[i])
    if i>0:
     reordenarcadena(i-1)

reordenarcadena(i-1)
print("".join(conjunto))
