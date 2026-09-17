#declaração de variáveis
a:int = 0
b:int = 0
c:int = 0 
#inicio
a = int(input("Informe o valor do primeiro cateto: "))
b = int(input("Informe o valor do segundo cateto: "))
c = ((a*a)+(b*b))**0.5

print("A hipotenusa é:", c)
#fim