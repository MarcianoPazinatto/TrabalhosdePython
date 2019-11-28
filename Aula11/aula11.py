#Aula 11

#Crie um programa que calcule
#O imposto ISS de um serviço de desenvolvimento de software utilizar metodos


from calculo_iss import calculoiss

servico=float(input('Digite o valor a ser tributado em R$'))
iss_1=float(input('Digite a porcentagem a ser tributada em %'))

iss=iss_1/100

print(f'O valor do imposto da empresa sobre o serviço  de R${servico} calculando a porcentagem de %{iss_1} é R${calculoiss(iss,servico)}')
