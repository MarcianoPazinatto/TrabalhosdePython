from aula import Calc

class Teste:
    def __init__(self):
        self.calc = Calc(1,1)

    def teste_soma(self):
        try:
            assert self.calc.soma() == 2
        except AssertionError:
            print(" teste soma falhou")
        else:
            print("teste soma passou")

    def teste_subtrair(self):
        try:
            assert self.calc.subtracao() == 0
        except AssertionError:
            print("Teste subtração falhou")
        else:
            print("Teste subtração passou")
    def teste_multiplicacao(self):
        try:
            assert self.calc.multiplicacao() == 1
        except AssertionError:
             print("teste de multiplicação falhou")
        else:
             print("Teste de multiplicação passou")

    def teste_divisao(self):
        try:
            assert self.calc.divisao() == 1
        except AssertionError:
            print("Teste de divisão falhou")
        else:
            print("teste de divisão foi um sucesso")

    def teste_set(self):
        try:
            self.calc.set_n1(10)
            self.calc.set_n2(20)
            assert self.calc.get_n1()==10
            assert self.calc.get_n2()==20
        except AssertionError:
            print("Teste set falhou")
        else:
            print("teste set passou")

    def teste_get(self):
        try:
            assert self.calc.get_n1()==10
            assert self.calc.get_n2()==20
        except AssertionError:
            print("get não passou no teste")
        else:
            print("get passou no teste")

teste = Teste()

teste.teste_divisao()
teste.teste_soma()
teste.teste_subtrair()
teste.teste_multiplicacao()
teste.teste_set()
teste.teste_get()

