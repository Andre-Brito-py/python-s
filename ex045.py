maior = 0
homem = 0
menina = 0

while True:
    sexo = str(input('Qual o seu sexo? [M/F] ')) .upper() .strip()
    while sexo not in('M', 'F'):
        print('Resposta invalida, tente novamente')
        sexo = str(input('Qual o seu sexo? [M/F] ')) .upper() .strip()
    idade = int(input('Qual a sua idade? '))

    if idade >= 18:
        maior += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        menina += 1

    continuar = str(input('Deseja continuar? [S/N] ')) .upper() .strip()
    while continuar not in('S', 'N'):
        print('Resposta invalida, tente novamente')
        continuar = str(input('Deseja continuar? [S/N] ')) .upper() .strip()
    if continuar == 'N':
        break


print(f'\n{maior} pessoas são maiores de idade')
print(f'{homem} são do sexo masculino')
print(f'{menina} pessoas do sexo feminino tem menos de vinte anos')