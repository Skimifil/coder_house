class Conta:

    def __init__(self, saldo, titular):
        self.saldo = saldo
        self.titular = titular

    def depositar(self, deposito):
        self.saldo += deposito
        print(f"Você tem {self.saldo} em conta")

    def sacar(self, saque):
        if saque <= self.saldo:
            self.saldo -= saque
            print(f"Você sacou {saque} e agora esta com {self.saldo}")
        else:
            print(f"Você {self.saldo}, não pode sacar o valor {saque}")
