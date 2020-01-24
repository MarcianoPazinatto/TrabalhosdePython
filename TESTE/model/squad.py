from model.linguagem import Linguagem
from model.framework import Framework
from model.sgbd import Sgbd

class Squad:

    def __init__(self):
        self.id = 0
        self.nome = ''
        self.descricao= ''
        self.numeropessoas = 0
        self.linguagembackend = Linguagem()
        self.frameworkfrontend = Framework()
        self.sgbd = Sgbd()

    def __str__(self):
        return f'{self.id};{self.nome};{self.descricao};{self.numeropessoas};{self.linguagembackend};{self.frameworkfrontend};{self.sgbd}'