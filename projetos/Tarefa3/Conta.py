# 3.Crie uma classe Conta com atributos titular e saldo.

class Conta:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de {valor} realizado. Novo saldo: {self.saldo}")

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente.")
        else:
            self.saldo -= valor
            print(f"Saque de {valor} realizado. Novo saldo: {self.saldo}")


conta = Conta(input("Informe o nome do titular da conta: "), float(input("Informe o saldo inicial: ")))
conta.depositar(float(input("Informe o valor a ser depositado: ")))
conta.sacar(float(input("Informe o valor a ser sacado: ")))