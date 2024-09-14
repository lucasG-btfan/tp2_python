"""19- Cree una clase OperacionMatematica con dos atributos valor1 y valor2 y un atributo de nombre operación.
Agregue a la clase los siguientes 5 métodos e implemente la lógica correspondiente:
sumarNumeros()
restarNumeros()
multiplicarNumeros()
dividirNumeros()
El quinto método será el siguiente:
aplicarOperacion(operacion){
…………………..
}
Cree una clase Calculo que contenga un método main, donde cree una instancia de la clase OperacionMatematica, 
asigne 2 valores para las variables de la instancia y ejecute la función aplicarOperacion, pasando como 
parámetro primero “+”, después “-”, a continuación “*” y finalmente “/”. Muestre por pantalla el resultado de las operaciones."""


class operacionMatematica:
    total = 0
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2

    def sumarNumeros(self):
        total = self.valor1 + self.valor2
        print(self.valor1, '+', self.valor2, '=', total)
        return total
    
    def restarNumeros(self):
        total = self.valor1 - self.valor2
        print(self.valor1, '-', self.valor2, '=', total)
        return total
    
    def multiplicarNumeros(self):
        total = self.valor1 * self.valor2
        print(self.valor1, '*', self.valor2, '=', total)
        return total
    
    def dividirNumeros(self):
        total = self.valor1 / self.valor2
        print(self.valor1, '/', self.valor2, '=', total)
        return total

    def aplicarOperacion(self, operacion):
        
        if operacion == '+':
            return self.sumarNumeros()
        elif operacion == '-':
            return self.restarNumeros()
        elif operacion == '*':
            return self.multiplicarNumeros()
        elif operacion == '/':
            return self.dividirNumeros()
        

class calculo:
    def main(self):
        nuevaOperacion = operacionMatematica(10, 5)
        nuevaOperacion.aplicarOperacion('+')
        nuevaOperacion.aplicarOperacion('-')
        nuevaOperacion.aplicarOperacion('*')
        nuevaOperacion.aplicarOperacion('/')

        
calc = calculo()
calc.main()
