#Faça um menu interativo que tenha: Cadastro da Banda, Cadastro do album, cadastro da música, sair
# o Menu deve ser executado até que se escolha a opção sair.
#Cada opção deve ser mostradaquando selecionado a opção sair, deverá aparecer na tela as informações das bandas cadastradas, albuns e músicas.
lista_banda=[]
lista_album=[]
lista_musica=[]

menu='''
*************************************************
*             Cadastro de bandas                *
*************************************************
1........Cadastro da Banda
2........Cadstro do Album
3........Cadastro da Música
4........Sair

Digite a opção: '''
while True:
    opcao=input(menu)
    if opcao=='1':
        a=input('Digite a banda:')
        lista_banda.append(a)        
          
    elif opcao=='2':
        b=input('Digite o album')
        lista_album.append(b)        

    elif opcao=='3':
        c=input('Digite a musica')      
        lista_musica.append(c)  
            
    elif opcao=='4':
        print(f'Bandas {lista_banda}') 
        print(f'Albuns {lista_album}')
        print(f'Músicas {lista_musica}')   
        break
    else:
        print('Opção errada')  
    