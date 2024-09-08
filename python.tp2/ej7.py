cadena=input("Diga una frase: ")
cadena=cadena.upper()
cantidadcadena=len(cadena)
cantidadvocales=0
i=0
def averiguarcantidaddevocales(caracter):
        global cantidadvocales        
        match caracter:
            case "A":
                cantidadvocales+=1
            case "E":
                cantidadvocales+=1
            case "I":
                cantidadvocales+=1
            case "O":
                cantidadvocales+=1
            case "U":
                cantidadvocales+=1
while i!=len(cadena):
     averiguarcantidaddevocales(cadena[i])
     i+=1
    
          
print(f"La frase tiene una longitud de {cantidadcadena} y posee {cantidadvocales} vocales")
