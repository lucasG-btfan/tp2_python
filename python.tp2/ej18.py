"""18- En la clase FuncionesPrograma codifique una método getFechaDate estática
que reciba como parámetro 3 valores enteros, día, mes, anio y retorne la fecha
de tipo date correspondiente."""
def doubleCheck(x, y, z):
    # Validar el año
    if z <= 0:
        print("ERROR: intente otro valor para el año")
        z = int(input("Ingrese el año: "))

    # Validar el mes
    if y <= 0 or y > 12:
        print("ERROR: intente otro valor para el mes")
        y = int(input("Ingrese el mes: "))

    # Validar el día
    if x <= 0 or x > 31:
        print("ERROR: intente otro valor para el día")
        x = int(input("Ingrese el día: "))
    elif y == 2 and x > 28:
        print("ERROR: intente otro valor para el día")
        x = int(input("Ingrese el día: "))
    elif y in [4, 6, 9, 11] and x > 30:
        print("ERROR: intente otro valor para el día")
        x = int(input("Ingrese el día: "))

    return x, y, z

# Pedir al usuario que ingrese el año, mes y día
year = int(input("Ingrese el año: "))
month = int(input("Ingrese el mes: "))
day = int(input("Ingrese el día: "))

# Llamar a la función para validar los valores
day, month, year = doubleCheck(day, month, year)

print(f"Fecha válida: {day}/{month}/{year}")
