#declaração de variáveis
a1:int = 0# angulo 1
a2:int = 0# angulo 2
a3:int = 0# angulo 3
#inicio
a1 = int(input("Informe o valor do primeiro ângulo: "))
a2 = int(input("Informe o valor do segundo ângulo: "))
a3 = 180 -  (a1+a2)
print("O valor do terceiro ângulo deverá ser:", a3)
#fim