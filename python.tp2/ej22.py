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
