"""Codifique un programa que solicite el ingreso de un numero decimal y asigne el mismo a una variable valorDecimal, 
aplique las operaciones de CASTING para convertir la variable a los siguientes tipos de datos, short, int, long, float 
investigue las diferentes formas de lograr la conversión. Muestre por pantalla el resultado de las conversiones."""

num_str= str (input ("ingrese un numero decimal: "))
print(num_str)
valorDecimal= float(num_str)
print("El numero en decimal es: ",valorDecimal)
numEnt = int(valorDecimal) 
print ("El numero en entero es: ",numEnt)
print("La cantidad de digitos son: ",len(num_str))
