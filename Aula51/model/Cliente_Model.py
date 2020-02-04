class ClienteModel:
    def __init__(self, nome, sobrenome, idade, sexo, id=0):
        self.id = id
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.sexo = sexo
