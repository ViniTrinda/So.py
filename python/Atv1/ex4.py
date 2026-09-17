#declaração de variáveis
temp: int = 0 # temperatura em Celsius
tempF: float = 0.0 # temperatura em Fahrenheit
#inicio

temp = int(input("Digite a temperatura em Celsius: "))
tempF = (((9*temp) + 160) / 5)
print("A temperatura em Fahrenheit é: ", tempF)

#fim