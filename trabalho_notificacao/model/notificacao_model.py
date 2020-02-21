class NotificacaoModel:

    def __init__(self,dados):
        self.dados = dados
        self.id = None
        self.pessoa_id = None
        self.data_evento = None
        self.comentario = None
        self.tipo_evento = None


    def tratar_dados(self):
        self.id = self.dados[0]
        self.pessoa_id = self.dados[1]
        self.data_evento = self.dados[2]
        self.comentario = self.dados[3]
        self.tipo_evento = self.dados[4]


    def serialize(self):
        return {
            "id": self.id,
            "pessoa_id": self.pessoa_id,
            "data_evento": str(self.data_evento),
            "comentario": self.comentario,
            "tipo_evento": self.tipo_evento
        }

