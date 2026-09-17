#declaração de variáveis

atual:int = 0
nasc:int = 0

#inicio

atual = int(input("Insira o ano atual: "))
nasc = int(input("Insira o ano de nascimento: "))

print("Idade:", (atual-nasc), "\nIdade em 17 anos:", ((atual-nasc) + 17))

#fim