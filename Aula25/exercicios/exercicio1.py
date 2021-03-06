# Aula 21 - 12-12-2019


# Cliente.....

# Crie uma classe cliente.
# Use os seguintes atributos: codigo cliente(int), nome, idade(int), telefone, email, endereço
# Use o seguinte atributo de estado: crédito em R$, saldo R$, 
#                                    cliente_devedor(True/False)
# O atributo cliente_devedor deve ser True toda vez que o saldo negativo for menor 
# ou igual ao crédito. 
# Para o atributo cliente_devedor voltar a ser False o cliente deve pagar sua divida
# ficando com o saldo igual a 0 ou positivo.



# Como metodo use:
class Cliente:
    def __init__(self,codigo, nome, idade, telefone, email, endereco):
        self.codigo = codigo
        self.nome = nome
        self.idade = idade
        self.telefone = telefone
        self.email = email
        self.endereco = endereco        

        self.credito = None
        self.saldo = None
        self.cliente_devedor = None



    def atualizar (self):
                  
        self.nome = input('Digite o nome: ')
        self.idade = int(input('Digite o nome: '))
        self.telefone = input('Digite o nome: ')
        self.email = input('Digite o nome: ')
        self.endereco = input('Digite o nome: ')      

        
        '''
        Este metodo serve para atualizar o cadastro do cliente. 
        Os dados que podem ser atualizados são: 
        nome, idade(int), telefone, email, endereço
        '''        

    def limite_credito(self,valor):

        self.credito -= valor
        self.saldo += valor
        while self.credito >= -10:
            self.cliente_devedor = False
        self.cliente_devedor = True    

        '''
        O crédito é o valor máximo que o cliente pode ter de saldo negativo.
        Este metodo, altera o valor tanto para aumentar o crédito quanto para 
        diminuir ou eliminar o crédito.

        Este valor deve ser passado como número negativo (ex: -50.00) para o atributo
        credito

        Se diminuir o crédito (exemplo de -50 para -10) e o 
        cliente ficar com o saldo menor que o crédito (exemplo saldo = -20 e cédito -10)
        o cliente_devedor fica True

        Se o cliente_devedor estiver True, o crédito pode ser diminuido porem não aumentado.
        
        '''
        pass

    def dinheiro(self,valor):
        valor=float(input('Digite o valor do emprestimo: '))                
        
        '''
        Este metodo serve para adicionar/remover valor em R$ para o atributo saldo para 
        o cliente.
        Esta função revebe o valor como parametro. Se o valor for positivo, o saldo
        aumenta, se o valor for negativo o saldo diminui. 
        
        O cliente não pode ter seu saldo menor que o crédito. Então se o valor exceder
        deve retornar False e a operação fica cancelada.
        (Exemplo: limite do cartão de crédito)

        Caso o valor não exceda o crédito a operação será realizada, o valor do saldo
        irá diminuir e deve retornar True

        Se o cliente_devedor estiver True o dinheiro só poderá receber valores positivos.

        Se o cliente_devedor estiver True e o cliente depositar dinheiro suficiente para
        o saldo ficar maior ou igual a 0 o cliente_devedor deve ser alterado para False.
        '''
        

    def __eq__(self,valor):
        '''
        Este metodo deve comparar se o valor do código do cliente é igual ao valor.
        Se positivo ele retorna True caso contrário retorna False
        '''
        pass

    def __srt__(self):
        '''
        Este metodo deve retornar uma string com todos os dados do cliente.
        Use f-string para interpolar o texto com as variáveis
        '''
        pass



if __name__ == "__main__":

    '''
    Use este if para fazer os testes com a classe.
    Este if pergunta se este arquivo está sendo executado diretamente.
    Caso positivo o código será executado.
    '''
    pass

a = Cliente()
a.atualizar()