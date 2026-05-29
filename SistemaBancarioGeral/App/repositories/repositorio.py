class Repositorio:

    def __init__(self):
        self.contas = []

    def salvar(self, conta):
        self.contas.append(conta)

    def listar(self):
        return self.contas