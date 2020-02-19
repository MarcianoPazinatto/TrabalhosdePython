from aula import Calc

class Teste:
    def __init__(self):
        c = Calc(2,3)


    def soma(self):
        try:
            assert self.soma() == 5
        except:
