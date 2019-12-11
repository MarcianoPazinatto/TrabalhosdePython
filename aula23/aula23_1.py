
# texto='lalala,lololo,lululu'
# print(texto.split(','))

# def nosso_split(txt,sep):
#     # return txt.split(sep)
#     result=[]
#     contador=0
#     ultima_pos_separador=0
#     for char in txt:
#         if char==sep:
#             result.append(txt[ultima_pos_separador:contador])
#             ultima_pos_separador=contador+1
#         contador+=1
#     if ultima_pos_separador<len(txt)    
#         result.append(txt[ultima_pos_separador:])
#     return result    


# print(nosso_split(texto,','))    

diasdecadames={
    1:31,
    2:28,
    3:31,
    4:30,
    5:31,
    6:30,
    7:31,
    8:31,
    9:30,
    10:31,
    11:30,
    12:31,   
}

# qual_mes=int(input('Digite o numerodo mês(1..12):'))

# print(f'o mes', qual_mes,'tem',diasdecadames[qual_mes],'dias')
# print(f'Dias que faltam para o fim do ano, a partir do mês informado')

# print(sum(list(diasdecadames.values())[qual_mes-1:]))
# ############################################################################
# total=0
# for mes in range(qual_mes,12+1):
#     total+=diasdecadames[mes]
# print('modo estruturado')
# print('total de dias atéo fim do ano', total)

for chave in diasdecadames:
    print('chave na linha', chave)
    print('valor', diasdecadames[chave])

for chave, valor in diasdecadames.items():
    print('chave',chave,'valor',valor)
#######################################################for em tupla
# tupla=('texto',5.1, 42, int, str, list)
tupla=('lalala','lololo','lululu')
for isto in tupla:
    print(type(isto))
    print(isto)