num = int(input('Digite um numero para ver sua taboada de multiplicação! '))
for valor in range(1, 11):
    print('{} x {} = {}' .format(num, valor, num * valor))