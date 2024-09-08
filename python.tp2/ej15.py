# Utilizo "None" por si una función retorna un valor que no tiene importancia

def buscar_numero(lista, numero_usuario):
    if numero_usuario in lista:
        return numero_usuario
    else:
        return None

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numero_usuario = int(input("Ingrese un numero para saber si es parte de la lista: "))

resultado = buscar_numero(lista, numero_usuario)

if resultado == None:
    print("El numero ", numero_usuario,  " no está en la lista.")
else:
    print("El numero ", numero_usuario,  " está en la lista.")

# Tambien "None" puede ser utilizado para inicializar una variable, para valores ausentes en lineas de datos,
# como caso base de una recursión, como control de funcionamiento de un programa, etc.
