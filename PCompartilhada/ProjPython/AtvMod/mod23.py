# Declaração de Variáveis
a = 0
b = 0
c = 0 
d = 0
res = ''

def calc():
    global a, b, c, d, res
    if d <= a:
        res = (d, a, b, c)
    elif d <= b and d > a:
        res = (a, d, b, c)
    elif d > b and d <= c:
        res = (a, b, d, c)
    else:
        res = (a, b, c, d)
    
    print(res)

def main():
    global a, b, c, d
    a = int(input('Digite o valor de a: '))
    b = int(input('Digite o valor de b: '))
    c = int(input('Digite o valor de c: '))
    d = int(input('Digite o valor de d: '))
    calc()

if (__name__ == '__main__'):
    main()