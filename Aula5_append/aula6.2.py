print('cadastrar produtos Mercado Tech')
d=0
list=[]
while d!=4:
    prod=input("Digite um produto")
    print('1.Adicionar Produto','2.Mostrar Produto','3.Mostrar Categoria','4.Sair')
    if d==1:
        list.append(prod)
    if d==2:
        print(list)   
    if d==4:
        exit()
    
print('cadastrar produtos Mercado Tech')
produto=input('digite o produto')
categoria=int(input('Informe 1 se for alcoólico e 2 se não for'))
if categoria==1:
    print(f'O nome é {produto} é alcoólico')

if categoria==2:
    print(f'o {produto} não é alcoólico')