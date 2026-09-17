#variaveis
horas = 0.0
valH  = 0.0
percD = 0
qntD  = 0
Sal   = 0.0

#Inicio

horas = float(input())
valH  = float(input())
percD = int(input())
qntD  = int(input())

Sal   = ((horas * valH) * ((100 - percD)/100) + (100*qntD)) 
#       ((salario bruto) * (Salario com desconto(%/100)) + (adicional de dependentes))  
print(Sal)

#Fim