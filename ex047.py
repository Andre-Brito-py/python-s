cont = ('zero', 'um', 'dois', 'três',
        'quatro', 'cinco0', 'seis',
        'sete', 'oito', 'nove0', 'dez')

while True:
    num = int(input('Digite um numero de 0 a 10: '))
    if 0 <= num <= 10:
        break
    print('Numero invalido, tente novamente.', end = ' ')

print(f'Você digitou {cont[num]}')