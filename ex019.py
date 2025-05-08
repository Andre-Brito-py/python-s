d = float(input('Por quantos quilometros você ficará conosco nesta viagem? '))
if d <= 200:
    v = float(d * 0.50)
    print('Sua viagem tem o valor de {:.2f}' .format(v))
if d > 200:
    v = float( d * 0.45)
    print('Sua viagem tem o valor de {:.2f}' .format(v))