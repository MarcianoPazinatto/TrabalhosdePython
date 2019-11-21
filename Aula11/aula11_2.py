#crie um programa que calcule a rentabilidade anual de um investimento 
# baseando-se em sua retabilidade mensal(juros compostos)
#a rentabilidade deve ser apresentada em % e em R$ utilizar métodos

from calculo2 import calculo_juros,lucro #importa as funções da aba calculo2

investimento=float(input('Digite o valor do investimento em R$: '))#recebe o valor do investimento
porcentagem=float(input('Digite a porcentagem aplicada em %: '))#recebe o valor da porcentagem do juros

porce=(porcentagem/100)#divide por 100 a porcentagem para permitir o calculo
cal=calculo_juros(investimento,porce)#dou uma variavel para o método para poder armazenar e utilizar em outras funções, (se não der a váriavel vai dar erro de float e função)
lu=lucro(investimento,cal)
print(f'Investindo o valor R${investimento} calcularemos a taxa {porcentagem}%, receberemos R${cal}, o lucro é R${lu}')

'''taxa=(investimento*100)/lu
print(f'A taxa de juros do período é {taxa}')'''