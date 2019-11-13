#--- Exercício 1 - Listas
#--- Escreva programa que leia o nome de 10 alunos
#--- Armazene os nomes em uma lista
#--- Imprima a lista

'''lista=['Manoel','Manolo','José','Josefino','Lukan','Lucas','Luana','Marluce','Zeniva','Barbara']'''

lista=[]
for i in range(0,10):    
    lista.append(input('Digite o nome: '))

print(lista)
