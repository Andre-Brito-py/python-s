pets = {}
animais = []
soma = media = 0

while True:
    resposta = str(input('Você tem um cachorro, ou um gato? [C/G] ')) .upper() .strip()
    if resposta == 'G':
        pets['Gatos'] = resposta
    if resposta == 'C':
        pets['Cachorros'] = resposta

    while resposta not in ('C', 'G'):
        print('Resposta invalida, tente novamente!')
        resposta = str(input('Você tem um cachorro, ou um gato? [C/G] ')) .upper() .strip()
        if resposta == 'N':
            break
    pets['idade'] = int(input('Qual a idade do seu pet? '))
    soma += pets['idade']

    animais.append(pets.copy())
    pets.clear()

    media = soma / len(animais)

    continuar = str(input('Deseja continuar? [S/N] ')) .upper() .strip()
    while continuar not in ('S', 'N'):
        print('Resposta invalida, tente novamente!')
        continuar = str(input('Deseja continuar? [S/N] ')) .upper() .strip()
    if continuar == 'N':
        break

print('=-' * 30)
print(f'Ao todo {len(animais)} animais cadastrados')
print(f'A média das idades é de {media} anos')
for pets in animais:
    if 'Gatos' in pets:
        print(f'A idade do gatinho cadastrado é {pets['idade']}')
for p in animais:
    if p['idade'] >= media:
        for k, v in p.items():
            print(f'  Os animais mais velhos que a media são: {k} = {v}')
        print()
