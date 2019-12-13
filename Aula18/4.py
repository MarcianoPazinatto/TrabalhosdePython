# Aula 18 - 03-11-2019

# interação de lista com o for

# Usando o comando for vamos fazer uma interação de varialvel tipo coleção. A interação é (simplificadamente) 
# percorer toda a variavel e isolar seu valores.

# 1.1 Com a seguinte lista, use o for para interar esta tupla  e apresentar (usando o f-string) O nome da cerveja, 
# tipo da cerveja, o IBU da cerveja e o preço dela.

cerveja = (('marca', 'tipo', 'ibu','preço'),
           ('Skol','IPA','ultra-leve',3.50),
           ('Brahma','lager','leve/media',3.45),
           ('Kaiser','Americam Larger','leve',2.35),
           ('Sol','larger mão','agua',1.19)
          )


# 1.2 Crie uma função que receba esta tupla e devolva uma lista com um dicionários referenciando cada uma destas 
# cervejas.

# cabe = cerveja[0]# pega apenas a primeira parte
# dados= cerveja[1:]#pega a segunda parte em diante

# for dados_cerveja in dados:
#     print(f'{cabe[0]},{dados_cerveja[0]}')
#     print(f'{cabe[1]},{dados_cerveja[1]}')
#     print(f'{cabe[2]},{dados_cerveja[2]}')    
#     print(f'{cabe[3]},{dados_cerveja[3]}')    

# print('\n\n')
   


def cerv(cerveja):
    lista=[]
    for j in range(len(cerveja)):
        dicionario={'marca':cerveja[j][0],'tipo':cerveja[j][1], 'ibu':cerveja[j][2], 'preço':cerveja[j][3]}
        lista.append(dicionario)
    return lista   

print(cerv(cerveja))  

  