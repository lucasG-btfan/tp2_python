def convertir_texto(texto):
    valores = []

    for letra in texto:
        valores.append(ord(letra))

    return valores

var1=str(input("ingrese 1 o mas palabra/s: "))
var2= var1.replace("a","e")
print(var2)
resultados = convertir_texto(var2)
print(resultados)

