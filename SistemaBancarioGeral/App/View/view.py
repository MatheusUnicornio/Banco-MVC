class ObtemDados:

    def obter_nome(self):
        return input('Digite seu nome: ')

    def obter_cpf(self):
        return input('Digite seu CPF: ')

    def obter_saldo(self):
        return float(input('Digite seu saldo: '))

    def exibir_dados(self, conta):
        print('\n SUA CONTA: ')

        print(f'Cliente: {conta.cliente.nome}')
        print(f'CPF: {conta.cliente.cpf}')
        print(f'Conta: {conta.numero}')
        print(f'Agência: {conta.agencia}')
        print(f'Saldo: R$ {conta.saldo}')