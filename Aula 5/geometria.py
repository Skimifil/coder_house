from retangulo import Retangulo
from conta_banco import Conta

primeiro_retangulo = Retangulo(3,6)
primeiro_retangulo.area()
primeiro_retangulo.perimetro()

meu_primeiro_saque = Conta(12, "Rafa")
meu_primeiro_saque.depositar(12)
meu_primeiro_saque.sacar(4)