num = 0

while num <= 0:
    num = int(input("Ingrese un numero mayor a cero: "))
print('el numero elegido es', num)

def sumabilidad(numero):
    if numero == 0: return numero
    else:
        return numero + sumabilidad(numero - 1)
    

print("El total es", sumabilidad(num))