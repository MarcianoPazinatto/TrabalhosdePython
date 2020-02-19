class Calculadora:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def soma(self):
        return self.num1 + self.num2

    def sub(self, num1, num2):
        return num1 - num2

    def mult(self, num1, num2):
        return num1 * num2

    def div(self, num1, num2):
        return num1 / num2


c = Calculadora(2,3)

print(c.soma())
