"""23- Crea un programa donde se pida el ingreso de una cadena y por medio de recursión mostrar la cadena de forma inversa.
Ejemplo: Ingreso “computadora de escritorio”
Invertir cadena “oirotircse ed arodatupmoc”""""


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
