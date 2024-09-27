#12- Dada la cadena “hipopotamo”, extraer la cuarta y quinta letra.

cadena = "hipopotamo"
nueva_cadena = ""
for i in range(0, len(cadena)):  
    if i != 4 and i != 5:
        nueva_cadena = nueva_cadena + cadena[i]
        
print(nueva_cadena)
