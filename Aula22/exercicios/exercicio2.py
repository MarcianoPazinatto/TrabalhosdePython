# Aula 21 - 09-12-2019
# Como Tratar e Trabalhar Erros!!!

# Com base no seguinte dado bruto:

dadobruto = '1;Arnaldo;23;m;alexcabeludo2@hotmail.com;014908648117'

# 1) Faça uma classe cliente que receba como parametro o dado bruto.
# 2) A classe deve iniciar (__init__) guardando o dado bruto nume variável chamada self.dado_bruto
# 3) As variáveis  código cliente (inteiro), nome, idade (inteiro), sexo, email, telefone
# devem iniciar com o valor None
# 4) Crie um metodo que pegue o valor bruto e adicione nas variáveis:
# código cliente (inteiro), nome, idade (inteiro), sexo, email, telefone
# convertendo os valores de string para inteiros quando necessários. 
# (Faça da forma que vocês conseguirem! O importante é o resultado e não como chegaram nele!)
# 5) Crie um metodo salvar que pegue os seguintes dados do cliente e salve em um arquivo. 
# código cliente (inteiro), nome, idade (inteiro), sexo, email, telefone
# 6) crie um metodo que possa atualizar os dados do cliente (código cliente (inteiro), 
# nome, idade (inteiro), sexo, email, telefone). Este metodo deverá alterar tambem o dado bruto para
# que na hora de salvar o dado num arquivo, o mesmo não estaja desatualizado.

class Cliente:

    def __init__(self,dadobruto):
        self.cod=None       
        self.nome=None
        self.idade=None
        self.sexo=None
        self.email=None
        self.telefone=None
        self.dado_bruto=dadobruto

    def listar(self):
        lista = self.dado_bruto.strip().split(';')
        self.cod = int(lista[0])
        self.email = (lista[4])
        self.nome = (lista[1]) 
        self.idade = int(lista[2])
        self.sexo = (lista[3])
        self.telefone = (lista[5])

    def salvar(self,nome,atributo = 'a'):   
        arquivo = open ('Exer{nome}.txt',atributo)
        #texto = f'{self.cod};{self.nome};{self.email}{self.idade};{self.telefone};{self.sexo}'
        texto = f'{self.dado_bruto}\n'
        arquivo.write(texto)
        arquivo.close()

    def atualizar(self):
        self.nome = input('Digite o novo nome: ')
        self.idade = int(input(' digite a idade: '))
        self.sexo = input('Digite o sexo: ')
        self.email = input('Digite o e-mail: ')
        self.telefone = input('Digite o novo telefone: ') 
        self.dado_bruto = f'{self.cod};{self.nome};{self.email}{self.idade};{self.telefone};{self.sexo}' 

pessoa = Cliente(dadobruto)
pessoa.listar()
pessoa.salvar(nome = 1)
pessoa.atualizar()

print(f'codigo: {pessoa.cod} Nome: {pessoa.nome}, Idade: {pessoa.idade} Sexo: {pessoa.sexo} Telefone: {pessoa.telefone} email {pessoa.email}')


