# Declaração de Variáveis
a = 0
b = 0
res = ""

def calc():
    global a, b, res
    if((a > b and a % b == 0) or (b > a and b % a == 0)):
        res = "O maior eh divisivel pelo menor"
    elif a == b:
        res = "Valores iguais"
    else:
        res = "O maior nao eh divisivel pelo menor"
    
    print(res)

def main():
    global a, b
    a = int(input('Digite o valor de a: '))
    b = int(input('Digite o valor de b: '))
    calc()

if (__name__ == '__main__'):
    main()