
valor_1 = int(input('Digite um valor: '))
valor_2 = int(input('Digite outro valor: '))
valor_3 = int(input('Mais um valor: '))
valor_4 = int(input('Último valor: '))


valores = (valor_1, valor_2, valor_3, valor_4)

par = 0
for numero in valores:
    if numero %2 == 0:
        par += 1
print(f'{par} valores são par')

nove = valores.count(9)
if nove > 0:
    print(f'O número 9 foi selecionado {nove} vezes')
else:
    print(f'O numero 9 não foi selecionado')

if 3 in valores:
    posicao = valores.index(3)
    print(f'A posição em que o numero 3 foi digitada é {posicao + 1}')
else:
    print('O numero 3 não foi selecionado')