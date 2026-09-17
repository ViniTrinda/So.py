#declaração de variáveis
tempo:int = 0
velm:int = 0 
kmr:int = 0

#inicio
tempo = int(input("informe a duração da viagem em horas: "))
velm = int(input("informe a velocidade media(km/h): "))
kmr =  tempo * velm

print("Esta viagem gastou um total de", (kmr/12),"litros")

#fim