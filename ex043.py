num = 0

while True:
    num = int(input('Digite um numero para ver a sua tabuada! (digite um negativo para parar):'))
    if num < 0:
            break
    print(f'\nTabuada do {num}\n')
    print('-' * 30)
    for i in range(1, 11):
        print(f'{num} x {i} = {num * i}')
    
print('Programa tauaba encerrado. Volte sempre!')