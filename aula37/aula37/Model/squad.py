class Squad:
    def __init__(self):
        id = 0
        nome = ''
        descricao = ''
        numeropessoas = 0
        linguagembackend = ''
        frameworkfrontend = ''

    def __str__(self):
        return f'{self.id};{self.nome};{self.descricao};{self.numeropessoas};{self.linguagembackend};{self.frameworkfrontend}'