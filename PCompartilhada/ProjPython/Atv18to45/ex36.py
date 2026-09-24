#variaveis
n = 0
res = 0.0
ifat = 0.0

#Inicio
res = 1.0
n = int(input())

for i in range(1, n + 1):
    ifat = 1.0
    for j in range(1, i + 1):
        ifat = ifat * j
    res = res + (1 / ifat)

print(res)

#Fim