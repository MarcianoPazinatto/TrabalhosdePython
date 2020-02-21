from flask_restful import Resource
from trabalho_notificacao.dao.notificacao_dao import BaseNotificacao

dao = BaseNotificacao()

class BaseController(Resource):
    def __init__(self):
        self.dao = BaseNotificacao

    def get(self):
        return self.dao.lista()