#declaração de variáveis
qnth:int = 0
valh:int = 0
percd:int = 0
numd:int = 0

salbruto:int = 0
saliquido:float = 0.0
res:float = 0.0
#inicio
qnth = int(input("Informe a quantia de horas trabalhadas: "))
valh = int(input("Informe o valor por hora trabalhada: "))
percd = int(input("Informe o valor do desconto em porcentagem: "))
numd = int(input("Informe a quantia de dependentes"))


salbruto = qnth * valh
saliquido = salbruto - (salbruto* (percd/100))
res = saliquido + (numd*100)

print("O salario a receber será:", res)
#fim