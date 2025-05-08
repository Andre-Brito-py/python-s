import random

# Entrada
nomes = []

print('Digite os nomes, um por um. Quando terminar, digite "fim".')

while True:
    nome = input('Digite um nome: ')
    if nome.lower() == 'fim':
        break
    nomes.append(nome)

# Embaralhamento e exibição (saída)
if nomes:
    random.shuffle(nomes)  # Corrigido "shuff" para "shuffle"
    print('\nA ordem sorteada é:')
    for i, nome in enumerate(nomes, start=1):
        print(f'{i}º - {nome}')
else:
    print('Nenhum nome foi inserido para o sorteio')
