#variáveis
a: int = 0
b: int = 0
c: int = 0
delta: int = 0
x1: int = 0
x2: int = 0

#inicio
a = int(input("Digite o valor de a:"))
b = int(input("Digite o valor de b:"))
c = int(input("Digite o valor de c:"))

delta = (b*b) - (4*a*c)

if delta < 0:
    print("A equação não tem respostas reais.")
elif delta == 0:
    x1 = ((-b) + (delta ** 0.5)) / (2*a)
    x2 = ((-b) - (delta ** 0.5)) / (2*a)
    print("Raizes iguais: ", x1)
    

else:

    x1 = ((-b) + (delta ** 0.5)) / (2*a)
    x2 = ((-b) - (delta ** 0.5)) / (2*a)

    print('o valor de x1 é:', x1, '\no valor de x2 é:', x2)

     
#fim