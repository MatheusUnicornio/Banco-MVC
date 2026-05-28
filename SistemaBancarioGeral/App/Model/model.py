class Conta:
    def __init__(self, numero, agencia, cliente):
        self.saldo = 0
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []


class Banco:
    def __init__(self):
        self.contas = []

    def add_contas(self, conta):
        self.contas.append(conta)