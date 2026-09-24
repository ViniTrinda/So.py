#variaveis
n = 0
maior = 0
val1 = 0
val2 = 0
ver = False

#Inicio
val1 = int(input())
val2 = int(input())

if val1 > val2:
    n = val2
    maior = val1
else:
    n = val1
    maior = val2

for i in range(n + 1, maior):
    if i > 1:
        if i == 2:
            print(i)
        else:
            ver = True
            for j in range(3, i, 2):
                if (i % j == 0) or (i % 2 == 0):
                    ver = False
            if ver:
                print(i)

#Fim