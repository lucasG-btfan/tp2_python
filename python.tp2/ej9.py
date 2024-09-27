"""Recorre la cadena del ejercicio 6 y transforma cada 
carácter a su código ASCII. Muéstralos en línea recta, separados por un espacio entre cada carácter."""
def convertir_texto(texto):
    valores = []

    for letra in texto:
        valores.append(ord(letra))

    return valores

var1=str(input("ingrese 1 o mas palabra/s: "))
print(var2)
resultados = convertir_texto(var2)
print(resultados)

