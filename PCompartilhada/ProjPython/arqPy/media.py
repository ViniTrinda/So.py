import os

nm  = ''
nt1 = 0.0
nt2 = 0.0
nt3 = 0.0
nt4 = 0.0
md  = 0.0

dir: str   = ''
arq: str   = ''

def media (a,b,c,d):
    res = (a+b+c+d)/4
    return res


def setter():
    global nm, nt1, nt2, nt3, nt4, md
    
    nm = input('nome do aluno:')
    nt1 = int(input('nota 1:'))
    nt2 = int(input('nota 2:'))
    nt3 = int(input('nota 3:'))
    nt4 = int(input('nota 4:'))
    
    md = media(nt1,nt2,nt3,nt4)
    print("media do aluno: "+ str(md))
    
    cad(nm, nt1, nt2, nt3, nt4, md)

def cad(nm, nt1, nt2, nt3, nt4, md):
    global dir, arq
    dir = '/tmp/exercicios'
    arq = '/ex21.txt'
    linha = str(nm) + ';' + str(nt1) + ';' + str(nt2) + ';' + str(nt3) + ';' + str(nt4) + ';' + str(md) + ';\n'
    
    escreve(dir, arq, linha)
    
    
def escreve(dir, arq, linha):    
    arquivo  = ''
    tipo  = ''
    enc   = ''

    arquivo = dir + arq
    enc = 'utf-8'
    
    os.makedirs(dir, exist_ok = True)
    os.chmod(dir, 0o744)
    
    if (os.path.exists(dir) and os.path.isdir(dir)):
        if(os.path.exists(arquivo)):
            tipo = 'a'
        else:
            tipo = 'w'
            
        with open(arquivo, tipo, encoding = enc) as file:
            file.write(linha)
            
            
def ler():
    
    print('Conteudo dentro do arquivo: \n')
    global dir, arq
    arquivo = dir + arq
    if(os.path.exists(dir) and os.path.isdir(dir)):
        with open(arquivo) as file:
            for linha in file:
                print(linha, end='')
    else: 
        print("Dir invalido")
        
    print('')
        
        
def main():
    
    for contador in range(5):
        setter()
        ler()
        
if __name__ == '__main__':
    main()