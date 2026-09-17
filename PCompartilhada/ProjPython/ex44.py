#variaveis
base = 0
expoente = 0
res = 0

#Inicio
base = int(input())
expoente = int(input())

res = 1

for i in range(expoente):
    res = res * base

print(res)

#Fim