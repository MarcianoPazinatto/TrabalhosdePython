class Bin:

    def receber_dado_inteiro(self):
        while True:
            try:
                self.numero = int(input("Digite um número inteiro e positivo:"))
                break
            except ValueError:
                print("Digite um número decimal, inteiro e positivo: ")

    def tratar_para_binario_receber_na_lista(self):
        self.lista = []
        self.binario = bin(self.numero)[2:]
        print(self.binario)
        for i in self.binario:
            self.lista.append(i)
        return self.lista

    def reverter_paraeliminar_os_zeros(self):
        self.lista.reverse()
        self.juntar = ''.join(self.lista)
        self.juntar = int(self.juntar)
        self.juntar = str(self.juntar)
        # print(self.juntar)

    def contar_os_zeros(self):
        self.contador = 0
        for i in self.juntar:
            if i == '0':
                self.contador += 1
            else:
                pass
        return print(f'O total de zeros que tem o numero {self.binario} é {self.contador}')

    def fatiar(self):
        self.separar = self.juntar.split('1')
        # print(self.separar)
        self.tamanho = (len(max(self.separar)))
        print(f"O maior intervalo de zeros do número {self.binario} é {self.tamanho}")



b = Bin()
b.receber_dado_inteiro()
b.tratar_para_binario_receber_na_lista()
# print(b.tratar_para_binario_receber_na_lista())
b.reverter_paraeliminar_os_zeros()
b.contar_os_zeros()
b.fatiar()