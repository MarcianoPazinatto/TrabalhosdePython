def salvar_pessoa(pessoa_dicionario):
    nome=open('variosdados.txt','a')
    nome.write(f"{pessoa_dicionario['nome1']};{pessoa_dicionario['sobrenome']};{pessoa_dicionario['idade']}\n")
    nome.close()

def ler():
    lista=[]
    nome=open('variosdados.txt','r')
    for linha in nome:
        linha=linha.strip()
        lista_linha=linha.split(';')
        pessoa={'nome1':lista_linha[0],'sobrenome':lista_linha[1],'idade':lista_linha[2]}       
        lista.append(pessoa)
    nome.close()  
    return lista  

nome1=input('Digite um nome: ')
sobrenome=input('Digite o sobrenome: ')
idade=int(input('Digite sua idade: '))

pessoa={'nome1':nome1, 'sobrenome':sobrenome, 'idade':idade}

salvar_pessoa(pessoa)

#ler() 

#print(ler())
#lista=ler()
for p in ler():
    print(f"{p['nome1']}-{p['sobrenome']}-{p['idade']}")
