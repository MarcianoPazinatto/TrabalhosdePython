#exercício 3
#crie um programa para calculo de investiemnto
#solicitar valor a ser investido no tesouro selic
#considerar o valor do Selic hoje
#calcule o calor total até o vencimento do titulo
#utilizar metodos
print('\n'*2,'='*70,'\n')
cotas=float(input('Digite quantas cotas irão ser adiquiridas (1=1 cota) minimo(0.01=01%): '))
selic=float(input('\nDigite a taxa da selic: '))
tempo=int(input('\nDigite o tempo que irá ficar aplicado o valor do investimento \n(1) para um ano\n(2) para dois anos\n(3) para tres anos\n(4) para quatro anos\n(5) para cinco anos\n(6) para o tempo total: '))

print('\n'*2)
cotaz=10410*cotas
p_selic=selic/100
t_selic=p_selic+0.0002

if tempo==6:
    cotac=cotaz*((1+t_selic)**5.2767)
elif tempo==5:    
    cotac=cotaz*((1+t_selic)**5)
elif tempo==4:
    cotac=cotaz*((1+t_selic)**4)    
elif tempo==3:
    cotac=cotaz*((1+t_selic)**3)  
elif tempo==2:
    cotac=cotaz*((1+t_selic)**2)      
elif tempo==1:
    cotac=cotaz*((1+t_selic)**1)   
else:
    print('Periodo incorreto')

lucro=cotac-cotaz  


         
print(f'O valor total recebido no periodo foi R${cotac:.2f} e o lucro R${lucro:.2f}')

print('\n'*1,'='*70,'\n'*2)