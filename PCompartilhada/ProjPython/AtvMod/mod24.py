# Declaração de Variáveis
a = 0
res = ''

def calc():
    global a, res
    if (a % 2 == 0 and a % 3 == 0):
        res = "Eh divisivel por 2 e 3"
    else:
        res = "Nao eh divisivel por 2 e 3"
    
    print(res)

def main():
    global a
    a = int(input('Digite o valor de a: '))
    calc()

if (__name__ == '__main__'):
    main()