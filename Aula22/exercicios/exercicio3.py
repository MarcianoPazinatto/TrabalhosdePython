# Aula 21 - 09-12-2019
# # Como Tratar e Trabalhar Erros!!!


# Dica: O mais importante é conseguir fazer! Não importa como chegou ao resultado e sim o resultado!

# Dica2: na função .open() você pode escolher entre 'r' para ler, 'w' para sobrescrever e criar um 
# arquivo novo ou o 'a' que é abreveativo de append, onde ele inclui linha no final do arquivo.
# Você sabia que o 'r', 'w' e o 'a' são string que podem ser passadas via variável exemplo:

# atributo = 'r'
# nome_arquivo = 'cadastro'
# arquivo.open(f'exercicio/{nome_arquivo}.txt',atributo)



# 1) Crie uma classe cadastro.
# Esta classe deve abrir o arquivo cadastro2.txt e guardar os cadastro numa lista com dicionários.

# 2) crie o metodo salvar os dados dos clientes em um arquivo txt.
# 3) crie um metodo para cadastrar novos clientes. O código cliente é unico por pessoa, sendo assim não pode 
# se repetir.
# 3) Crie um metodo de consulta de cliente, mostrando os dados dele na tela.
# 4) Crie um metodo para atualizar o cadastro de um cliente qualquer pelo codigo cliente.
# Após atualizar, salvar todos no arquivo "cadastro_atualizado.txt" (use o 'w' para sobrescrever o arquivo.)
#
#  Observação: Use o try/filnaly para abrir e fechar os arquivos. Veja na aula 21- Ecessões como é!


# arqui=open('C:\Dados\GitHub\python\TrabalhosdePython\Aula22\exercicios\cadastro2.txt', 'r')
# print(arqui.readline())
# arqui.close()


class Cadastro:

    def __ini__ (self):
        pass
    def linha(self):
        lista=[]        
        arquivo = open('C:\Dados\GitHub\python\TrabalhosdePython\Aula22\exercicios\cadastro2.txt','r')
        for linhas in arquivo:
            linhas = linhas.strip().split(';')
            dicionario = {}
            dicionario['cod']=linhas[0]
            dicionario['nome']=linhas[1]
            dicionario['idade']=linhas[2]
            dicionario['sexo']=linhas[3]
            dicionario['email']=linhas[4]
            dicionario['cpf']=linhas[5]
        lista.append(dicionario)  
        arquivo.close()  
        return lista
        
        
        
a = Cadastro()
aa=a.linha()
print(aa)   




# #     def abrir(self):
# #         arquivo = open('cadastro2.txt','r')                
# #         arquivo.close()  


# a = Cadastro(cadastro)        
