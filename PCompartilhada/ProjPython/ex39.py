#variaveis
ant = 0
res = 0

#Inicio
ant = 1
res = ant

for i in range(64):
    res = ant * 2
    ant = res

print(res)

#Fim