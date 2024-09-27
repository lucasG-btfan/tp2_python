"""22- Suma los dígitos de un número ingresado por el usuario de forma recursiva.
Ejemplo: el usuario ingresa 1596
El programa debe sumar 1 + 5 + 9 + 6"""


def sumaDigitos(n):
    if n == 0:
        return 0
    else:
      #usamos modulo para ver los digitos  del num
        print("Los digitos a sumar son:", n%10)
        return n % 10 + sumaDigitos(n // 10)

# Ingresamos un valor
num = int(input("Ingrese un numero:"))
print("La suma de los digitos es:", sumaDigitos(num))
