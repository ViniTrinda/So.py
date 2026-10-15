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
    global dir, arq
    caminho = dir + arq
    if(os.path.exists(dir) and os.path.isdir(dir)):
        with open(caminho) as file:
            for biscoito in file:
                print(biscoito, end='')#printa todo o conteudo/elemento do arquivo, nesse caso, cada linha
                
                if('oito' in biscoito):# tem como fazer uma busca desse tipo e manipular elementos especificos
                    print(biscoito, end='')
                    #lembrando que, a principio, o arquivo nao existe e em nenhum momento, algo com 'oito' 'e inserido, portanto, o teste eh irracional
                    #posteriormente, o conteudo inserido no caminho anexado acima se limita somente a numeros, retorna false
                
        
    else: 
        print("Dir invalido")
        
  
def ler_conteudo():
    print('\nConteudo inserido:\n')
    
    global dir, arq, valor
    arquivo = dir + arq
    if(os.path.exists(dir) and os.path.isdir(dir)):
        with open(arquivo) as file:
            for linha in file:
                if(int(linha)%valor == 0): #printa somente o conteudo inserido no arquivo nessa execucao, em tese
                    print(linha, end='')
    else: 
        print("Dir invalido")


#==========================================================================================================================================================


def main():
    global valor
    valor = int(input())
    
    for contador in range (1,11):   # poderia ser 11, assim comecaria no 0 e iria ate o 10, 11 execucoes, porem, 
                                    #nesse caso, como nenhum usuario ativamente realiza as acoes, o resultado seria o mesmo
        res = mult(valor, contador)
        escreve(contador, res)

    ler()
        

if (__name__ == "__main__"):
    main()