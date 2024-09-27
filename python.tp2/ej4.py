"""4- Desarrolle un programa que ayude a una cajera a determinar el número de billetes y monedas 
que se necesitan de cada una de las siguientes denominaciones 200, 100, 50, 20, 10, 5, 2 y 1, y
monedas de 0.50, 0.25, 0.10 y 0.05 centavos para una cantidad de dinero dada. Ejemplo si la 
cantidad es 1390,55 se necesitan 6 billetes de 200, 1 billete de 100, 1 billete de 50, 2 billetes
de 20, 1 moneda de 0.50 y una moneda de 0.05 centavos. Plantee el algoritmo planteando métodos para su resolución."""


"""billetes = [200, 100, 50, 20, 10, 5, 2, 1]
monedas = [0.50, 0.25, 0.10, 0.05]

contador = 0

i = 0
num = float(input('Ingresa el precio: $'))

while num >= 1:
    if num % billetes[i] != num:
        contador += num // billetes[i]
        num = num % billetes[i]
        print("Cantidad de billetes de " + str(billetes[i]),"x" + str(int(contador)))
    contador = 0
    i += 1

i = 0
while num > 0 and num < 1:
    if num % monedas[i] != num:
        contador += num // monedas[i]
        num = num % monedas[i]
        print("Cantidad de monedas de ", monedas[i], str(int(contador)))
    contador = 0
    i += 1"""


import math
num=int(input("Ingrese una cantidad de dinero: "))
for billete in (200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.1, 0.05 ):
     cocientereal=num/billete
     cocienteaumentado= math.ceil(cocientereal) #lo redondeo hacia arriba porque se necesita
                                                #pagar con el total de billetes divisores más
                                                #  otro billete más que sería el que paga 
                                                #la parte menor, el resto.
     print(f"Debe pagar con {cocienteaumentado} billetes de ${billete}") 



# Porque no distingue entre 0.5 y 0.05