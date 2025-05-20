from time import sleep

ficha = []


while True:
    nome = str(input('Nome: '))
    nota_1 = float(input('Primeira nota: '))
    nota_2 = float(input('Segunda nota: '))
    media = (nota_1 + nota_2) / 2
    ficha.append([nome, [nota_1, nota_2], media])
    resposta = str(input('Deseja continuar? [S/N] ')) .upper() .strip()

    while resposta not in ('S', 'N'):
        print('Resposta invalida, tente novamente')
        resposta = str(input('Deseja continuar? [S/N] ')) .upper() .strip()
    if resposta in('N'):
        break

print('=-' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":<8}')
print('-' * 26)

for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    print('-' * 30)
    opc = int(input('Você deseja ver a nota de qual aluno? 777 para interromper: '))
    if opc == 777:
        print('Finalizando...')
        sleep(1)
        print('<<< Voltei sempre! >>>')
        break
    if opc <= len(ficha):
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
