from trabalho_notificacao.model.notificacao_model import NotificacaoModel


class BaseNotificacao:
    def pegar_dados(self):
        arquivo = open(r'C:\Users\Usuario\PycharmProjects\trabalhos\notificacao\notificacao.txt', 'r')
        self.lista = []
        for linha in arquivo:
            linha = linha.strip()
            lista_linha1 = linha.split(';')
            lista_linha = NotificacaoModel(lista_linha1)
            lista_linha.tratar_dados()
            list = lista_linha.serialize()
            self.lista.append(list)
        return self.lista

a = BaseNotificacao()

print(a.pegar_dados())

