import math

class Fraccion():

    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"
    

class OperacionesFraccion():

    @staticmethod
    def sumarFracciones(fraccion1, fraccion2):
        mcm = math.lcm(fraccion1.denominador , fraccion1.denominador)
        numresult = (fraccion1.numerador * (mcm // fraccion1.denominador)) + (fraccion2.numerador * (mcm // fraccion2.denominador))

        return Fraccion(numresult, mcm)
    @staticmethod
    def restarFracciones(fraccion1, fraccion2):
        mcm = math.lcm( fraccion1.denominador , fraccion1.denominador)
        numresult = (fraccion1.numerador * (mcm // fraccion1.denominador)) - (fraccion2.numerador * (mcm // fraccion2.denominador))
        return Fraccion(numresult, mcm)
    @staticmethod
    def multiplicarFracciones(fraccion1, fraccion2):
        denominador = fraccion1.denominador * fraccion2.denominador
        numresult = fraccion1.numerador * fraccion2.numerador

        return Fraccion(numresult, denominador)
    @staticmethod
    def dividirFracciones(fraccion1, fraccion2):
        numresult = fraccion1.numerador * fraccion2.denominador
        denominador = fraccion1.denominador * fraccion2.numerador

        if denominador == 0: 
            return print("La fraccion restultante tiene un denominador 0.")
        else:
            return Fraccion(numresult, denominador)
        
class Menu():
    @staticmethod
    def limpiar():
        print("Ingrese el numerador")
        num1 = int(input())
        denominador  = 0 
        while denominador == 0:
            print("Ingrese el denominador ")
            denominador = int(input())
        return Fraccion(num1, denominador)
    @staticmethod
    def aplicarOperacion(fraccion1, fraccion2):
        operacion = None
        while operacion != 7:
            print("---------------------------------")
            print("Porfavor ingrese que operacion desea ejecutar ")
            print(f"Los numeros actuales son {fraccion1} y {fraccion2} ")
            print("1 - Suma")
            print("2 - Resta")
            print("3 - Multiplicacion")
            print("4 - Division")
            print("5 - Cambiar numeros Fraccion 1")
            print("6 - Cambiar numeros Fraccion 2")
            print("7 - Salir")
            print("---------------------------------")
            operacion = int(input())

            match operacion:
                case 1:
                    fracSuma = OperacionesFraccion.sumarFracciones(fraccion1, fraccion2)
                    print(fracSuma)
                case 2:
                    fracResta = OperacionesFraccion.restarFracciones(fraccion1, fraccion2)
                    print(fracResta)
                case 3:
                    fracMult = OperacionesFraccion.multiplicarFracciones(fraccion1, fraccion2)
                    print(fracMult)
                case 4:
                    fracDiv = OperacionesFraccion.dividirFracciones(fraccion1, fraccion2)
                    print(fracDiv)
                case 5:
                    fraccion1.numerador = int(input("Porfavor ingrese el nuevo numerador de la fraccion 1 "))
                    fraccion1.denominador = int(input("Porfavor ingrese el nuevo denominador de la fraccion 1 "))
                case 6:
                    fraccion2.numerador = int(input("Porfavor ingrese el nuevo numerador de la fraccion 2 "))
                    fraccion2.denominador = int(input("Porfavor ingrese el nuevo denominador de la fraccion 2 "))
                case 7:
                    print("Saliendo del programa")


def main():
    acceso = Menu()
    fraccion1 = acceso.limpiar()
    fraccion2 = acceso.limpiar()
    acceso.aplicarOperacion(fraccion1, fraccion2)
main()

