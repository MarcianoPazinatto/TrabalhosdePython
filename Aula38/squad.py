p1 = [Nicole ,PHP, MySqlServer, React]
p2 = [Tiago,Java, PostgreSQL, VUE]
p3 = [Mateus ,Python, MongoDb, Angular]

class Squad:
    

    def __init__(self,person):  
        self.nome = None
        self.backend = None
        self.frontend = None
        self.dados = None
        self.person = person




# Nicole = PHP, MySqlServer, React
# Tiago = Java, PostgreSQL, VUE
# Mateus = Python, MongoDb, Angular.


#     def cadastrar(self,person,nome):
#
#         self.nome = input ('Digite o nome: ')
#         self.backend = input ('Digite a linguagem backend: ')
#         self.frontend = input ('Digite o frontend: ')
#         self.dados = input ('Digite o SGBD: ')
#         self.person = f'{self.nome};{self.backend};{self.frontend};{self.dados}'
#
#
#     def salvar(self,nome):
#         arquivo = open (f'{self.nome}.txt','a')
#         texto = f'{self.person}\n'
#         arquivo.write(texto)
#         arquivo.close()
#
#     def listar(self):
#         lista = self.person.strip().split(';')
#         self.nome = (lista[0])
#         self.backend = (lista[1])
#         self.frontend= (lista[2])
#         self.dados = (lista[3])
#
# p1 = Squad(person)
# p1.cadastrar(person, nome = 1)
# p1.salvar(nome = 1)
# print(f'{p1.nome},{p1.backend},{p1.frontend},{p1.dados}')
#
# p2 = Squad(person)
# p2.cadastrar(person, nome = 1)
# p2.salvar(nome = 1)
# print(f'{p2.nome},{p2.backend},{p2.frontend},{p2.dados}')
#
# p3 = Squad(person)
# p3.cadastrar(person, nome = 1)
# p3.salvar(nome = 1)
# print(f'{p3.nome},{p3.backend},{p3.frontend},{p3.dados}')


        
#         lista = []
#         for p in range(0,2):            
#             p1.self.nome = input ('Digite o nome: ')
#             p1.self.backend = input ('Digite a linguagem backend: ')
#             p1.self.frontend = input ('Digite o frontend: ')
#             p1.self.dados = input ('Digite o SGBD: ')
#             p.append(lista)
#         return lista   


# a = cadastrar()
# print(a)