"""
Simule o funcionamento de um banco digital e crie contas para reproduzir alguns
dos principais recursos. Um banco possui uma conta comum, que deve ter as
seguintes propriedades: números da agência e conta, nome do proprietário da
conta, renda mensal e saldo. A conta deve ter seu número gerado aleatoriamente
e precisa permitir a realização das seguintes operações:

- depósito;
- consulta do saldo disponível;
- saque.

O banco também disponibiliza uma linha de crédito especial pré-aprovado.
O saldo desse crédito é estabelecido aleatoriamente, no intervalo entre a renda
mensal e o dobro desse valor. Caso o cliente deseje sacar, ele precisa pagar
uma taxa de 1,99% por saque. Inclua as operações que julgar adequadas para
operar, satisfatoriamente, essa linha de crédito.
"""

from random import randint


class Conta:
    def __init__(self, agencia, conta, proprietario, renda, saldo):
        self.agencia = agencia
        self.conta = conta
        self.proprietario = proprietario
        self.renda = renda
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        return self.saldo

    def consultar_saldo(self):
        return self.saldo

    def sacar(self, saque):
        if self.saldo > 0:
            if saque <= self.saldo:
                self.saldo -= saque
                return f'Saldo atualizado: R${self.saldo}'
            else:
                return f'Saldo insuficiente'
        else:
            return f'Você não possui saldo em conta'

    def transferir(self, conta_destino, valor_transferencia):
        if self.saldo > 0 and valor_transferencia <= self.saldo:
            self.saldo -= valor_transferencia
            conta_destino.saldo += valor_transferencia
            return f'Transferência realizada com sucesso'
        else:
            return f'Saldo insuficiente. Transferência não realizada'

    def linha_credito(self, valor_solicitado):
        taxa = 1.99
        credito = randint(self.saldo, self.saldo * 2)
        if valor_solicitado <= credito:
            self.saldo += valor_solicitado - ((valor_solicitado * taxa) / 100)
            return f'Crédito depositado na conta {self.conta} de {self.proprietario} com sucesso'
        else:
            return f'Valor superior ao crédito pré-aprovado : R${credito}'


c1 = Conta(1, 1_000, 'Rafael', 12_000, 10_000)
c2 = Conta(1, 1_001, 'Camila', 12_000, 7_000)
c3 = Conta(1, 1_002, 'Giovanna', 5_000, 3_500)

# print(f'{c1.proprietario} - Renda R${c1.renda}')
# print(f'{c2.proprietario} - Renda R${c2.renda}')
print(f'{c3.proprietario} - Saldo R${c3.saldo}')
print(f'{c1.proprietario} - Saldo R$ {c1.consultar_saldo()}')
print(f'{c2.proprietario} - Saldo R$ {c2.consultar_saldo()}')
print(c1.transferir(c2, 2_000))
print('Após a transferência')
print(f'{c1.proprietario} - Saldo R${c1.saldo}')
print(f'{c2.proprietario} - Saldo R${c2.saldo}')

print(f'Antes da linha de crédito : R$ {c1.consultar_saldo()}')
print(c1.linha_credito(3_000))
print(f'Depois de pegar o crédito : R$ {c1.consultar_saldo()}')
'''
print(f'Antes do depósito: R${c1.saldo}')
c1.depositar(5_000)
print(f'Após o depósito: R${c1.saldo}')
print(f'Saldo atual: R${c1.consultar_saldo()}')

print('Após o saque')
print(c1.sacar(15_000))
print(c1.sacar(15_000))
'''
