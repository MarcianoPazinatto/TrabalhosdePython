lista=[]
dicionario={}
dicionario={'nome': 'Marciano','sobrenome':'Pazinatto'}
print(dicionario)
print(dicionario['sobrenome'])

nome='Marciano'
lista_notas=[10,20,30,50]
media = sum(lista_notas)/len(lista_notas)
situacao= 'Reprovado'
if media >=7:
    situacao='Aprovado'
dicionario_alunos= {'nome':nome, 'lista_notas':lista_notas, 'media': media, 'situacao':situacao}

print(f"{dicionario_alunos['nome']} - {dicionario_alunos['situacao']}")