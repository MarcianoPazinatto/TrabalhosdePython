dicionario_bandas={'nome':''}
dicionario_bandas['nome']= 'Calipso'
print(dicionario_bandas)
print('\n')
dicionario_bandas['nome']='Dejavu'

print(dicionario_bandas)
print('\n\n')

dicionario = {'nome':'Marciano', 'sobrenome':'Pazinatto'}#dicionário, chaves estipulando valores
print(dicionario)
print('\n')
dicionario['sobrenome']='Lima'
dicionario['CPF']='000.000.00.00'

print(dicionario)



lista_pessoa=[]
for i in range(1,11):#atribui os valores para 10 pessoas, fazendo um laço
    dicionario_pessoa={'nome':'','sobrenome':'','CPF':'','RG':''}#cria um dicionário com as chaves sem valores.
    dicionario_pessoa['nome']=input('digite o nome: ')
    dicionario_pessoa['sobrenome']=input('Digite o sobrenome: ')
    dicionario_pessoa['CPF']=input('Digite o cpf: ')
    dicionario_pessoa['RG']=input('Digite o rg: ')
    lista_pessoa.append(dicionario_pessoa)#coloca o dicionário dentro da lista