from trabalho_notificacao.dao.base_notification import BaseNotificacao


class NotificacaoDao(BaseNotificacao):
    def __init__(self):
        super().__init__()

    def listar (self):
        return self.lista

    def get_by_id (self, id):
        pass

    def post(self):
        pass

    def put (self):
        pass

    def delete (self,id):
        pass
