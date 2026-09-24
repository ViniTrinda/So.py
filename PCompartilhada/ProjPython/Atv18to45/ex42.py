#variaveis
res = 0.0
num = 0
den = 0.0

#Inicio
res = 0.0

for num in range(1, 51):
    den = float(2 * num - 1)
    res = res + (num / den)

print(res)

#Fim