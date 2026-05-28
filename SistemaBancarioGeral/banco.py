from abc import ABC, abstractmethod

class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass


class Conta:
    def __init__(self, numero, agencia, cliente):
        self.saldo = 0
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = Historico()

    def obter_saldo(self):
        return self.saldo

    @classmethod
    def nova_conta(cls, numero, agencia, cliente):
        return cls(numero, agencia, cliente)

    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            return True

    def depositar(self, valor):
        if valor <= 0:
            return False
        else:
            self.saldo += valor
            return True

    def exibir_dados(self):
        print(f'Cliente: {self.cliente.nome}')
        print(f'Número: {self.numero}')
        print(f'Agência: {self.agencia}')
        print(f'Saldo: R$ {self.saldo}')

class ContaCorrente(Conta):
    def __init__(self, numero, agencia, cliente, limite, limite_saques):
        super().__init__(numero, agencia, cliente)
        self.limite = limite
        self.limite_saques = limite_saques
    

class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        conta.depositar(self.valor)


class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        conta.sacar(self.valor)


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
        conta.historico.adicionar_transacao(transacao)

class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, data_nasc, endereco):
        super().__init__(endereco)

        self.nome = nome
        self.cpf = cpf
        self.data_nasc = data_nasc
