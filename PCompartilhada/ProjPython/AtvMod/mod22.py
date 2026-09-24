# Declaração de Variáveis
a = 0
b = 0 

def calc():
    global a, b
    if a > b:
        print(b, a)
    else:
        print(a, b)

def main():
    global a, b
    a = int(input('Digite o valor de a: '))
    b = int(input('Digite o valor de b: '))
    calc()

if (__name__ == '__main__'):
    main()