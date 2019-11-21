#exercício 3
#crie um programa para calculo de investiemnto
#solicitar valor a ser investido no tesouro selic
#considerar o valor do Selic hoje
#calcule o calor total até o vencimento do titulo
#utilizar metodos
cotas=float(input('Digite quantas cotas irão ser adiquiridas (1=1 cota) minimo(0.01=01%): '))
selic=float(input('Digite o valor da selic: '))


cotaz=10410*cotas
p_selic=selic/100
t_selic=p_selic+0.0002
cotac=cotaz*(t_selic**5.2767)
print(f'{cotac}')