#declaração de variáveis
depo: int = 0
poup: float = 0.0
#inicio
depo = int(input("Insira o valor do depósito: "))
poup = 0.013
print("Valor em poupança após um mês:", depo + (depo*poup))
#fim