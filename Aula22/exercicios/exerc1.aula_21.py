# Crie uma classe cliente
# deve ter como atributos: codigo, cpf, nome, idade, sexo
# como metodos: receber salario, comprar
# quando recebe aumenta o dinheiro da carteira.
# quando compra aumenta os bens e diminui o dinheiro na carteira
# se compra e não tiver dinheiro o suficiente deve diminuir o dinheiro da carteira e 
# aumentar a divida.
# para pagar a divida tem que ter dinheiro o suficiente na carteira
# atributos de estado: dinheiro na carteira, divida, bens

class Cliente:
    def __init__(self,codigo1,cpf1,nome1,idade1,sexo1):
        self.codigo=codigo1
        self.cpf=cpf1
        self.nome=nome1
        self.idade=idade1
        self.sexo=sexo1
        #######atributos de estado
        self.carteira=0
        # self.salario=0
        self.bens=None
        self.divida=0
        self.emprestimo=0

    def serv(self,serviço):
        if serviço== True:
            self.carteira+=2000
        else:
            self.carteira+=0

    def comp(self,comprar):
        if comprar==True:
            self.bens='comprei coisas'   
            self.carteira-=3000
        if self.carteira<=0:    
            self.divida+=3000
        else:
            self.divida==0

       

pessoa1=Cliente('2','4423432424','Marciano','18','M')
pessoa1.serv(False)
pessoa1.comp(True)

print(f'Bens: {pessoa1.bens}')
print(f'carteira: {pessoa1.carteira}')
print(f'divida: {pessoa1.divida}')
