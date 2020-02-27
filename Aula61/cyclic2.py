class Ciclo:


    def listas(self):
        self.A = [3, 8, 9, 7, 6]
        self.B = [1, 2, 3, 4]

    def escolher(self):
        while True:
            numerodevezes = int(input('Digite o numero de vezes que quer rotacionar a lista: '))
            self.listas = int(input('''Digite o valor 1 para lista [3, 8, 9, 7, 6]
                                                      2 para lista [1, 2, 3, 4]    ''')
            if self.listas == 1:
                for i in range(numerodevezes):
                    self.listas.insert(0, self.listas[-1])
                    self.listas.pop()
            print(self.listas)

        else:
            pass