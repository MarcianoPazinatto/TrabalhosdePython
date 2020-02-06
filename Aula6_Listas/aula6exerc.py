# Exercício 3
# Programa que leia as notas (4) de 10 alunos
# Armazene os nome e as notas em listas
# Imprima os nomes, médias e situação (Aprovado se > 7)

nomes = []
notas = []
a = 0
b = 1
c = 2
d = 3

for i in range(0,10):
    nomes.append(input(f'Digite o nome do aluno {i+1}: '))
    for j in range(0,4):
        notas.append(float(input(f'Digite a nota {j+1}: ')))

for alunos in nomes:
     media = (notas[a]+notas[b]+notas[c]+notas[d])/4
     print(f'\nNome: {alunos}')
     print(f'Média: {media}')
     if media >= 7:
          print('Aprovado!')
     else:
          print('Reprovado!')
     a = a+4
     b = b+4
     c = c+4
     d = d+4
