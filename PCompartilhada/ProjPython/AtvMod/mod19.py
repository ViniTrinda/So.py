# Declaração de Variáveis
a = 0.0
b = 0.0
res = ''

def calc():
    global a, b, res
    if a > b:
        res = a
    elif b > a:
        res = b
    else:
        res = "valores iguais"

def main():
    global a, b, res
    a = float(input('Digite o valor de a: '))
    b = float(input('Digite o valor de b: '))
    calc()
    print(res)

if (__name__ == '__main__'):
    main()