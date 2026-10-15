#ARQUIVO FEITO PARA ACOMPANHAR A VIDEO AULA E TESTAR AS OPERACOES, SEM FINALIDADE OU COERENCIA;
import os

valor: int = 0
dir: str   = ''
arq: str   = ''

def mult(a, b):
    res = a*b
    return res


def escreve(c, d):
    global dir, arq
    
    arquivo  = ''
    tipo  = ''
    enc   = ''
    linha = ''
    
    dir = '/tmp/exercicios'
    arq = '/ex34.txt'
    
    linha = str(d) + '\n'
    arquivo = dir + arq
    enc = 'utf-8'
    
    os.makedirs(dir, exist_ok = True)
    os.chmod(dir, 0o744)
    
    if (os.path.exists(dir) and os.path.isdir(dir)):
        if(os.path.exists(arquivo) and c > 0):
            tipo = 'a'
        else:
            tipo = 'w'
            
        with open(arquivo, tipo, encoding = enc) as file:
            file.write(linha)
    

    
def ler():
    print('\nConteudo inserido:\n')
    
    global dir, arq, valor
    caminho = dir + arq
    if(os.path.exists(dir) and os.path.isdir(dir)):
        with open(caminho) as file:
            for linha in file:
                if(int(linha)%valor == 0): #printa somente o conteudo inserido no arquivo nessa execucao
                    print(linha, end='')
    else: 
        print("Dir invalido")



def main():
    global valor
    valor = int(input())
    
    for contador in range (11):
        res = mult(valor, contador)
        escreve(contador, res)

    ler()
        

if (__name__ == "__main__"):
    main()