#variaveis
a = 0
b = 0
c = 0
d = 0

media = 0.0
#Inicio
a = int(input())
b = int(input())
c = int(input())
d = int(input())

media = (a + b + c + d) / 4

if media >= 6:
    print("APROVADO!")
elif media >= 3 and media < 6:
    print("EXAME")
else:
    print("RETIDO")
     
#Fim