class Squad:

    def __init__(self):
        self.id = 0
        self.sistema_banco = ''
        
    def __str__(self):
        return f'{self.id};{self.sistema_banco}'