dados = {}
dados['nome'] = str(input('Digite o nome do aluno: '))
dados['media'] = float(input(f'Digite a média do {dados['nome']}: '))

for chave, valor in dados.items():
    print(f'{chave} é igual a {valor}')

if dados['media'] <= 6:
    print('SItuação é igual a Reprovado')
elif dados['media'] >= 7:
    print('SItuação igual a Aprovado')