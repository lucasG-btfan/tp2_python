num3dig = input("Ingresa un numero de 3 digitos (100 - 999) ")

num = int(num3dig)
if num < 100 or num > 999:
    print("El numero ingresado no es un numero de 3 digitos.")
    exit()

# 563 // 100 = 5  +  56 % 10 = 6     + num % 10 = 3
suma = num // 100 + (num // 10) % 10 + num % 10
print(suma)

#################################################################################################

# Alternativa
# if len(num3dig) != 3:
#     print("El numero ingresado no es de 3 digitos.")
#     exit()

# suma = 0
# for i in num3dig:
#     print(i)
#     suma += int(i)
#print("La suma del numero ingresado es:", suma)