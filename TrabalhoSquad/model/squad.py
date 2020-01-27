from model.linguagem import Linguagem
from model.framework import Framework
from model.sgbd import Sgbd

class Squad:

    def __init__(self):
        self.id = 0
        self.nome = ''
        self.descricao= ''
        self.numeropessoas = 0
        self.linguagem = Linguagem()
        self.framework = Framework()
        self.sgbd = Sgbd()

    def __str__(self):
        return f'{self.id};{self.nome};{self.descricao};{self.numeropessoas};{self.linguagem};{self.framework};{self.sgbd}'