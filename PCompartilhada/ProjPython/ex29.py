#variaveis
tipo = 0
val  = 0.0
perc = 0

res = ""

#Inicio

while (tipo != 1) and (tipo !=2):
    tipo = int(input("Informe o tipo de investimento[1: Poupanca || 2: Renda Fixa]:"))
    
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

#Fim