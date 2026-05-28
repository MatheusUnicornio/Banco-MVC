from Model.model import Conta, Cliente

class Controller:
    def __init__(self, banco, view):
        self.banco =  banco
        self.view = view

    def criar_conta(self):

        nome = self.view.obter_nome()
        cpf = self.view.obter_cpf()
        saldo = self.view.obter_saldo()

        cliente = Cliente(nome, cpf)

        conta = Conta(numero=1, agencia='0001', cliente=cliente)

        conta.saldo = saldo

        self.banco.adicionar_conta(conta)

        self.view.exibir_conta(conta)