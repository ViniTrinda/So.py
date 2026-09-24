# Declaração de Variáveis
a = 0
b = 0
c = ''

def calc():
    global a, b, c
    if a > b:
        c = a - b
    elif b > a:
        c = b - a
    else:
        c = "valores iguais"

def main():
    global a, b, c
    a = int(input('Digite o valor de a: '))
    b = int(input('Digite o valor de b: '))
    calc()
    print(c)

if (__name__ == '__main__'):
    main()