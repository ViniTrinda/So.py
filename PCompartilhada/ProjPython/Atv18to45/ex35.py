#variaveis
a = 0
b = 0
res = 0

#Inicio
a = int(input())
b = int(input())

if a > b:
    for i in range(b, a):
        if i % 2 != 0:
            res += i
else:
    for i in range(a, b):
        if i % 2 != 0:
            res += i

print(res)

#Fim