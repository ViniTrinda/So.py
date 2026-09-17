#variaveis
a = 0 
b = 0
c = ''

#Inicio
a = int(input())
b = int(input())

if a > b:
    c = a - b
elif b > a:
    c = b - a
else:
    c = "valores iguais"
print(c)
#Fim