km = int(input('Qual foi a velocidade do carro? '))
v = km - 80
m = float(v * 7)
if v <= 0:
    print('Você está dentro do limite de velocidade')
else:
    print('Você ultrapassou o limite de velocidade e foi multado em R${:.2f}' .format(m))