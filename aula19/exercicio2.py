# Aula 19 - 04-12-2019
# Lista com for e metodos

cab = ['nome', 'telefone', 'email','idade']

pess   = [  ['Alex'   ,'Paulo'  ,'Pedro'  ,'Mateus' ,'Carlos' ,'João'   ,'Joaquim'],
            ['4799991','4799992','4799993','4799994','4799995','4799996','4799997'],
            ['a@a.com','b@b.com','c@c.com','d@d.com','e@e.com','f@f.com','g@g.com'],
            ['18'     ,'25'     ,'40'     ,'16'     ,'15'     ,'19'     ,'17'     ]   
        ]


# 1 - Usando estas 2 listas, fazer uma função que crie retorne uma lista com dicionários
# com os dados das pessoas com idade maior ou igua a 18 anos
#
#  2 - Imprima a lista resultante com um for imprimindo um dicionário em cada linha 
# (não prescisa usar o f-string, .format())
#
#  3 - Imprima a lista resultante com um for imprimindo um dicionário em cada linha 
# (usando o f-string)
#####################################1
def pessoas(pess):
    lista = []
    for p in range(len(pess[0])):#indice das pessoas
        dicionario = {}
        for i in range(len(pess)):#indice do cabeçalho
                dicionario[cab[i]]=pess[i][p]
        if int(dicionario['idade']) >= 18:
                lista.append(dicionario)
    return lista
print(pessoas(pess))  

a=pessoas(pess)
print(f'\n\n')
#####################################2
for p in a:
        print(p)

print(f'\n\n')
#####################################3
for pa in a:
        print(f'{pa}')



