#variaveis
a = 0
b = 0
res = ""
#Inicio
a = int(input())
b = int(input())

if((a>b and a%b == 0) or (b>a and b%a==0)):
    res = "O maior eh divisivel pelo menor"
elif a == b:
    res = "Valores iguais"
else:
    res = "O maior nao eh divisivel pelo menor"
    
print(res)

#Fim