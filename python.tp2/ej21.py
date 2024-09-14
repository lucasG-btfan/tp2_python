"""21- Codifique un programa que solicite un número entero mayor a cero y que mediante
recursión sume todos los números números naturales desde el número ingresado hasta 1.
Ejemplo: Ingreso 10
El programa debe sumar 10 + 9 + 8 +7 +6 + 5 + 4 + 3 + 2 + 1"""

num = 0

while num <= 0:
    num = int(input("Ingrese un numero mayor a cero: "))
print('el numero elegido es', num)

def sumabilidad(numero):
    if numero == 0: return numero
    else:
        return numero + sumabilidad(numero - 1)
    

print("El total es", sumabilidad(num))
