class Controller:
    def __init__(self, service, view):
        self.service = service
        self.view = view

    def criar_conta(self):

        nome = self.view.obter_nome()
        cpf = self.view.obter_cpf()
        saldo = self.view.obter_saldo()

        conta = self.service.criar_conta(nome, cpf, saldo)

        self.view.exibir_conta(conta)