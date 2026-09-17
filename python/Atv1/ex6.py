#declaração de variáveis
x: int = 0
y: int = 0
z: int = 0 
#inicio
x = int(input("Insira o valor para x: "))
y = int(input("Insira o valor para y: "))

z = x
x = y
y = z

print("Agora, o valor de x é:", x, "\nAgora, o valor de y é:", y)

#fim