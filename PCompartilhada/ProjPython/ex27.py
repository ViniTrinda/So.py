#variaveis
numv = 0 
ext  = 0 
dur  = 0

res = ""
#Inicio

numv = int(input())
ext = int(input())
dur = int(input())

res = f"Velocidade Media: {float(((numv*ext)/1000))}km/{(dur//60)}:{dur%60:02}h"


print(res)

#Fim