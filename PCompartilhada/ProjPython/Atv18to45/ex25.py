#variaveis
inic = 0.0
fim  = 0.0

res = 0.0

#Inicio
inic = float(input("informe o horario de inicio(HH.MM): "))
inic = int(((inic//1) * 60) + ((inic - (inic//1))*100)) # transforma em minutos
            #horas*60 + minutos(em decimais) * 100
fim = float(input("informe o horario de encerramento(HH.MM): "))
fim = int(((fim//1) * 60) + ((fim - (fim//1))*100)) # transforma em minutos

if(fim < inic):
    res = 1440 - (inic - fim)
else:
    res = fim - inic

res = (res//60) + ((res%60)/100)

print("Duracao total[HH.MM]: ",f"{res:05.2f}")

#Fim