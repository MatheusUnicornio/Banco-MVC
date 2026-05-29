from App.Model.cliente import Cliente
from App.Model.conta import Conta


class Servico:

    def __init__(self, repositorio):
        self.repositorio = repositorio

    def criar_conta(self, nome, cpf, saldo_inicial):

        cliente = Cliente(nome, cpf)

        conta = Conta(numero=1, agencia='0001', cliente=cliente)

        conta.saldo = saldo_inicial

        self.repositorio.salvar(conta)

        return conta
