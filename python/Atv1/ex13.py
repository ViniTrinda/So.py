#declaração de variáveis
qntA: float = 0 #quantidade de alimento
#inicio
qntA = float(input("Insira a quantidade de alimento(KG): "))

print("Essa quantidade de alimento poderia ser consumida em:", ((qntA*1000)/50), "dias")
#fim