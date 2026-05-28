from banco import Historico


class Conta:
    def __init__(self, numero, agencia, cliente):
        self.saldo = 0
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.saldo = 0
        self.historico = Historico()

    def depositar(self, valor):

        if valor <= 0:
            return False
        else:
            self.saldo += valor
            return True

    def sacar(self, valor):

        if valor > self.saldo:
            return False
        else:
            self.saldo -= valor
            return True
