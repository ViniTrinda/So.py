#variaveis
maior = 0.0
menor = 0.0
n = 0.0

#Inicio
maior = 0.0
menor = 0.0

for i in range(100):
    n = float(input())
    
    if maior == 0 or menor == 0:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

print(f"Maior: {maior}\nMenor: {menor}")

#Fim