# Declaração de Variáveis
a = 0
b = 0
c = 0
d = 0
media = 0.0

def calc():
    global a, b, c, d, media
    media = (a + b + c + d) / 4

    if media >= 6:
        print("APROVADO!")
    elif media >= 3 and media < 6:
        print("EXAME")
    else:
        print("RETIDO")

def main():
    global a, b, c, d
    a = int(input('Digite o valor de a: '))
    b = int(input('Digite o valor de b: '))
    c = int(input('Digite o valor de c: '))
    d = int(input('Digite o valor de d: '))
    calc()

if (__name__ == '__main__'):
    main()