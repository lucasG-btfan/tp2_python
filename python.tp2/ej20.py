
# Función para asegurarse de que el valor no sea 0
def NumN(x):
    if x != 0:
        return x
    else:
        x = int(input("ERROR ingrese otro valor: "))
        return NumN(x)

# Función para sumar fracciones
def suma_d_fracc(a, b, c, d):
    num1 = (a * d) + (c * b)
    num2 = b * d
    print(f"{num1}/{num2}")

# Función para restar fracciones
def restar_fracc(a, b, c, d):
    num1 = (a * d) - (c * b)
    num2 = b * d
    print(f"{num1}/{num2}")

# Función para multiplicar fracciones
def mult_fracc(a, b, c, d):
    num1 = a * c
    num2 = b * d
    print(f"{num1}/{num2}")

# Función para dividir fracciones
def div_fracc(a, b, c, d):
    num1 = a * d
    num2 = b * c
    print(f"{num1}/{num2}")

class operacionesFraccion:
    def __init__(self, numerador1, denominador1, numerador2, denominador2, fraccion1, fraccion2, OperacionesFraccion):
        self.numerador1 = numerador1
        self.denominador1 = denominador1
        self.numerador2 = numerador2
        self.denominador2 = denominador2
        self.fraccion1 = fraccion1
        self.fraccion2 = fraccion2
        self.OperacionesFraccion = OperacionesFraccion

    # Realizamos un switch case para elegir la operación aritmética
    def switch_case(self):
        match self.OperacionesFraccion:
            case 1:
                print(f"{self.fraccion1} + {self.fraccion2} = ", end="")
                suma_d_fracc(self.numerador1, self.denominador1, self.numerador2, self.denominador2)
            case 2:
                print(f"{self.fraccion1} - {self.fraccion2} = ", end="")
                restar_fracc(self.numerador1, self.denominador1, self.numerador2, self.denominador2)
            case 3:
                print(f"{self.fraccion1} * {self.fraccion2} = ", end="")
                mult_fracc(self.numerador1, self.denominador1, self.numerador2, self.denominador2)
            case 4:
                print(f"{self.fraccion1} / {self.fraccion2} = ", end="")
                div_fracc(self.numerador1, self.denominador1, self.numerador2, self.denominador2)
            case _:
                print("Por favor, ingrese un número correcto, hubo un error")

def main():
    # Ingresamos valores para el numerador y el denominador de la primera fracción
    numerador1 = int(input("Ingrese el primer numerador: "))
    numerador1 = NumN(numerador1)
    denominador1 = int(input("Ingrese el primer denominador: "))
    denominador1 = NumN(denominador1)
    fraccion1 = f"{numerador1}/{denominador1}"
    print("La primera fracción es:", fraccion1)

    # Ingresamos valores para el numerador y el denominador de la segunda fracción
    numerador2 = int(input("Ingrese el segundo numerador: "))
    numerador2 = NumN(numerador2)
    denominador2 = int(input("Ingrese el segundo denominador: "))
    denominador2 = NumN(denominador2)
    fraccion2 = f"{numerador2}/{denominador2}"
    print("La segunda fracción es:", fraccion2)

    # Solicitamos al usuario que ingrese la operación que desea realizar
    OperacionesFraccion = int(input("Ingrese un número por la operación que desea realizar: +(1); -(2); *(3); /(4): "))

    # Creamos una instancia de operacionesFraccion y llamamos a switch_case
    operacion = operacionesFraccion(numerador1, denominador1, numerador2, denominador2, fraccion1, fraccion2, OperacionesFraccion)
    operacion.switch_case()

# Llamamos a main
if __name__ == "__main__":
    main()

