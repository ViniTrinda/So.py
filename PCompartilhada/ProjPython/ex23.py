#variaveis
a = 0
b = 0
c = 0 
d = 0

res = ''

#Inicio

a = int(input())
b = int(input())
c = int(input())
d = int(input())

if d <= a:
    res = d, a, b, c
elif d <= b and d > a:
    res = a, d, b, c
elif d > b and d <= c:
    res = a, b, d, c
else:
    res = a, b, c, d
    
print(res)

#Fim