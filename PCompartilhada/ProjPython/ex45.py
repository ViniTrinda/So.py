#variaveis
res = 0.0
num = 0
den = 0.0

#Inicio
res = 0.0

for num in range(1, 16):
    den = float(num * num)
    if num % 2 != 0:
        res = res + (num / den)
    else:
        res = res - (num / den)

print(res)

#Fim