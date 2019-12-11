# Aula 21 - 09-12-2019
# Como Tratar e Trabalhar Erros!!!

# Com base no seguinte dado bruto:
#     def db(self,lista):
#         lista=[]
#         self.dadobruto=self.dadobruto.split(';')
#         lista.append(self.dadobruto)
#         return lista


# lista=Cliente
# print
lista=[]
dadobruto = '1;Arnaldo;23;m;alexcabeludo2@hotmail.com;014908648117'


# 1) Faça uma classe cliente que receba como parametro o dado bruto.
# 2) A classe deve iniciar (__init__) guardando o dado bruto nume variável chamada self.dado_bruto
# 3) As variáveis  código cliente (inteiro), nome, idade (inteiro), sexo, email, telefone
# devem iniciar com o valor None
# 4) Crie um metodo que pegue o valor bruto e adicione nas variáveis:
# código cliente (inteiro), nome, idade (inteiro), sexo, email, telefone
# convertendo os valores de string para inteiros quando necessários. 
# (Faça da forma que vocês conseguirem! O importante é o resultado e não como chegaram nele!)
#5) Crie um metodo salvar que pegue os seguintes dados do cliente e salve em um arquivo. 
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

    def salvar(self,dadobruto):   
        lista = self.dado_bruto.strip().split(';')     
        arquivo = open('cad.txt','w')
        arquivo.write(dadobruto) 
        arquivo.close()  




a = Cliente(dadobruto)
a.listar()
a.salvar(dadobruto)
print(a.cod)
print(a.email)
print(f'Nome: {a.nome}, Idade: {a.idade} Sexo: {a.sexo} Telefone: {a.telefone}')






# lista1 = []
# lista1.append(Cliente(dadobruto))
# lista1[0].listar()
# print(lista1[0].cod+9)


         

       

    
      
            



        


