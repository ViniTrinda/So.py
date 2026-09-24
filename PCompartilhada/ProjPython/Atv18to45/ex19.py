#variaveis
a = 0.0
b = 0.0

res = ''
#Inicio
a = float(input())
b = float(input())


if a > b:
    res = a
elif b > a:
    res = b
else:
    res = "valores iguais"

print(res)
#Fim