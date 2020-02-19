from aula import Calc

class Teste:
    def __init__(self):
        self.c = Calc(3,1)


    def soma(self):
        try:
            assert self.c.soma() == 4
        except AssertionError:
            print("Falha no teste de soma")
        else:
            print("Teste soma passou")

    def subtracao(self):
        try:
            assert  self.c.subtracao() == 2
        except AssertionError:
            print("Falha no teste de subtração")
        else:
            print("Teste de Subtração passou")

    def multiplicacao(self):
        try:
            assert self.c.multiplicacao() == 3
        except AssertionError:
            print("Falha no teste de multiplicação")
        else:
            print("Teste de multiplicação passou")

    def divisao(self):
        try:
            assert self.c.divisao() == 3
        except AssertionError:
            print("Falha no teste de divisão")
        else:
            print("Teste de divisão passou")


t = Teste()

t.soma()
t.divisao()