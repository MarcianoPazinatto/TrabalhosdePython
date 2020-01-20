class Endereco:
    id = 0
    rua = ''
    bairro = ''
    cidade = ''
    

    def exportar_txt(self, lista_enderecos):
        #----- Cria um arquivo e atribui a uma variável 'arquivo'
        with open('33-Aula33/Aula33-4/endereco.txt','a') as arquivo:
            #---- Percorre a lista de dicionário e salva no arquivo em formato pré-definido
            for e in lista_enderecos:
                arquivo.write(f"{str(e)}\n")
    
    def __str__(self):
        return f'{self.id};{self.rua};{self.bairro};{self.cidade}'