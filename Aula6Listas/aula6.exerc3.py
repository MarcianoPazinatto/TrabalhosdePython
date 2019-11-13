#--- Exercício 3 - Foreach
#--- Escreva programa que leia as notas (4) de 10 alunos
#--- Armazene as notas e os nomes em listas
#--- Imprima:
#           1- O nome dos alunos 
#           2- Média do aluno
#           3- Resuldo (Aprovado>=7.0)

listanome=[]
listanotas=[]

for i in range(0,4):
    listanotas.append(input('Digite as notas: '))
   

for i in range(0,2):
     listanome.append(input('Digite a lista de nomes: '))

print(listanotas)  
print(listanome)   