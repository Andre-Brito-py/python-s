total = 0
mil = 0
mais_barato = ''
preco_mais_barato = 0
primeiro_produto = True

while True:
    produto = str(input('Informe o nome do produto: ')) .strip()
    preco = float(input('Informe o preço do produto: R$ '))
    total += preco

    if preco >= 1000:
        mil += 1
    
    if primeiro_produto:
        mais_barato = produto
        preco_mais_barato = preco
        primeiro_produto = False
    elif preco < preco_mais_barato:
        mais_barato = produto
        preco_mais_barato = preco


    continuar = str(input('Deseja continuar? [S/N] ')) .upper() .strip()
    while continuar not in('S', 'N'):
        print('Resposta invalida, tente novamente')
        continuar = str(input('Deseja continuar? [S/N] ')) .upper() .strip()
    if continuar == 'N':
        break

print(f'O total dos produtos é R${total:.2f}')
print(f'{mil} produtos estão acima de R$ 1000.00')
print(f'O produto mais barato foi "{mais_barato}", custando R${preco_mais_barato:.2f}')