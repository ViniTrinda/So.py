def calc(tipo):

        if (tipo == 1) or (tipo == 2):
            val  = float(input("Informe o valor do investimento: "))

            if(tipo == 1):
                perc = 3
            elif tipo == 2:
                perc = 5


            res = f"Valor depois de um mes: {(val * ((perc+100)/100)):.2f} R$"
            print(res)
        else:

            print("informe um valor valido! (1 ou 2)\n\n")


def main():
    tipo = int(input("Informe o tipo de investimento[1: Poupanca || 2: Renda Fixa]:"))

    calc(tipo)
    
    
if __name__ == '__main__':
    main()