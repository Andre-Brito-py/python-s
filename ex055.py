pessoas = []
dados = []
quantas = 0

while True:
    dados.append(str(input('Digite seu nome: ')))
    dados.append(float(input('Digite seu peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    continuar = str(input('Deseja continuar? [S/N] ')) .upper() .strip()
    while continuar not in('S', 'N'):
        print('Resposta invalida, tente novamente')
        continuar = str(input('Deseja continuar? [S/N] ')) .upper() .strip()
    if continuar == 'N':
        break

maior = max(pessoas)
menor = min(pessoas)

pos_maior = [i for i, v in enumerate(pessoas) if v == maior]
pos_menor = [i for i, v in enumerate(pessoas) if v == menor]

quantas = len(pessoas)

print('=-' * 30)
print(f'A quantidade de pessoas cadastradas foi: {quantas}')
print(f'O maior peso é {maior[1]:}Kg. Peso de {maior[0]}')
print(f'O menor peso é {menor[1]}Kg. Peso de {menor[0]}')