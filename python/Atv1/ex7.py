#declaração de variáveis
c: int = 0 #comprimento
l: int = 0 #largura
a: int = 0 #altura

#inicio
c = int(input("Defina o valor para o comprimento: "))
l = int(input("Defina o valor para a largura: "))
a = int(input("Defina o valor para a altura: "))

print("O volume do paralelepípedo é o seguinte:", ((c*l) * a), "unidades cubicas")
#fim