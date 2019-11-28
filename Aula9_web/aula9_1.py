#---------------------------------

from calculo_imposto import calculo_inss, calculo_irrf

salario=float(input('Digite o salario'))

inss=calculo_inss(salario)  
irff=calculo_irrf(salario,inss)

salario_liquido= salario -irrf - inss 
print(f'Inss{inss}')
print(f'irrf{irrf}')
print(f'Seu salario liquido é {salario_liquido}')



       