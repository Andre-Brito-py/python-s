galera = []
pessoa = {}
soma = media = 0

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('sexo: [M/F]')).upper().strip()[0]
    while pessoa['sexo'] not in ('M', 'F'):
        print('Resposta inválida, tente novamente')
        pessoa['sexo'] = str(input('sexo: [M/F] ')).upper().strip()[0]

    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())

    resposta = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    while resposta not in ('S', 'N'):
        print('Resposta inválida, tente novamente')
        resposta = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if resposta == 'N':
        break

media = soma / len(galera)

print('=-' * 30)
print(f'Ao todo temos {len(galera)} pessoas cadastradas')
print(f'A média das idades é de {media:.2f} anos')
print(f'As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f"{p['nome']} ", end='')
print()

print('Lista das pessoas acima da média:')
for p in galera:
    if p['idade'] >= media:
        for k, v in p.items():
            print(f'  {k} = {v}')
        print()
