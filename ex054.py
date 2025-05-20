num = []
pares = []
impares = []

while True:
    numero = int(input('Digite um número: '))
    num.append(numero)

    while True:
        resposta = input('Deseja continuar? [S/N]: ').strip().upper()
        if resposta in ('S', 'N'):
            break
        else:
            print('Resposta inválida. Tente novamente.')

    if resposta == 'N':
        break

# Classificação dos números (fora do loop)
for v in num:
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)

print('=-' * 30)
print(f'A lista com todos os números é: {num}')
print(f'A lista com os números pares é: {pares}')
print(f'A lista com os números ímpares é: {impares}')
print('=-' * 30)
