#variaveis
venM  = 0
precA = 0.0
perc  = 0
precN = 0.0

#Inicio

venM  = int(input())
precA = int(input())

if (venM < 500) and (precA < 30):
    perc = 10
elif (venM >= 500 and venM < 1000) and (precA >= 30 and precA < 80 ):
    perc = 15
else:
    perc = -5
    
precN = precA * ((perc + 100)/100)
print(f"{precN:.2f}")
#Fim