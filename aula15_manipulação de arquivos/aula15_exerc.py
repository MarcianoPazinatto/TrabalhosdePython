nome1=input('Digite um nome: ')
nome=open('Nome.txt','a')
#nome.write(f'{nome1}\n')
nome.write('{}\n'.format(nome1))
nome.close()

nome=open('Nome.txt',)
for linha in nome:
    print(linha)
nome.close()