#criar um programa para o cadastro do cliente
#para cadastro de clientes deve pedir os seguintes dados:
#codigo do cliente, cpf, nome completo, dasta de nascimento, estado, cidade, cep, bairro, rua
#numero da casa, complemento

#dados_cliente=['codigo-cliente','cpf','nome_completo','data_de_nascimento','estado','cidade','cep','bairro','rua','numero_casa','complemento']
#lista=[]

#################################################adicionando os dados um por um dentro de uma lista


#for i in dados_cliente:
#    lista.append=input(f'{i}')


#dicionario={}

###################################################adicionando o dicionario dentro de uma lista
#for i in dados_cliente:
#    lista.append=input(f'{i}')    
#lista.append(dicionario)

#print(lista)
#print('\n')
#print(dicionario)
def cadastro_cliente(numero):
    dados_cliente=['codigo-cliente','cpf','nome_completo','data_de_nascimento','estado','cidade','cep','bairro','rua','numero_casa','complemento']
    lista=[]

       for j in range(numero):
        dicionario={}

        for i in dados_cliente:
            dicionario[i]=input(f'{i}')
        lista.append(dicionario)
    return lista    


numero=int(input('Digite o numero de cadastros: '))
lista_cadastro=cadastro_cliente(numero) 

#######função para salvar o arquivo

arquivo = open('clientes.txt','a')
for cliente in arquivo:
    cliente_chave=list(cliente.keys())
    for chaves in cliente
    salvar=f'{cliente['codigo_cliente'];}'