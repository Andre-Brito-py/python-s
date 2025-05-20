valores = []

for cont in range(1, 6):
    valores.append(int(input('Digite um valor: ')))

maior = max(valores)
menor = min(valores)

pos_maior = [i for i, v in enumerate(valores) if v == maior]
pos_menor = [i for i, v in enumerate(valores) if v == menor]

print('=-' * 30)
print(f'você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} na(s) posição(êos) {pos_maior}...')
print(f'O menor valor digitado foi {menor} na(s) posição(êos) {pos_menor}...')

print('-' * 30)
print('Cheguei ao final da lista')
print('-' * 30)
