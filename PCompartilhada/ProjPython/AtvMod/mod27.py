def calc(volt, tam, temp):
    m = (volt*tam)/1000
    durac = temp/60
    res = f'{m/durac}/{temp//60}:{temp%60}'
    print(res)

def main():
    volt = int(input())
    tam = int(input())
    temp = int(input())
    calc(volt,tam,temp)
    

if (__name__ == '__main__'):
    main()