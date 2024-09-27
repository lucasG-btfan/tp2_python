billetes = [200, 100, 50, 20, 10, 5, 2, 1]
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
    i += 1

# Porque no distingue entre 0.5 y 0.05