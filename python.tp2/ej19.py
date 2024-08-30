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