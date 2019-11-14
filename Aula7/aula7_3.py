#----Exercício 1 - Dicionário
#----Escreva programa que leia os dados de 11 jogadores
#----Jogador: nome, posicao,numero,pernaboa
#----Crie um dicionário para armazenar os dados
#----Imprima os jogadores e seus dados

jogadores=[]#----cria uma lista, para poder colocar os valores do dicionário de todos os jogadores
jogador={'nome':'','pos':'','num':'','per':'' }#----cria o dicionário, com os valores vázios
for i in range(1,3):
    jogador['nome']=(input('Nome: '))
    jogador['pos']=(input('Posição: '))
    jogador['num']=(int(input('NUmero: ')))
    jogador['per']=(input('Perna boa: '))
    jogadores.append(jogador)#---adiciona o dicionário dentro da lista

print(jogadores)