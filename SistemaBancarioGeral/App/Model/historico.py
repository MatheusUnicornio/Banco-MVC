class Historico:
    def __init__(self):
        self.transacao = []

    def adicionar_transacao(self, transacao):
        self.transacao.append(transacao)

    def listar_transacao(self):
        return self.transacao