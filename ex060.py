from datetime import datetime

dados = {}
dados['nome'] = str(input('Nome: '))
nascimento = int(input('Nascimento: '))
dados['idade'] = datetime.now().year - nascimento
dados['ctps'] = str(input('Carteira de Trabalho (0 não tem): '))

if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: R$'))
    dados['Aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)

print('=-' * 30)

for chave, valor in dados.items():
    print(f' - {chave} tem o valor {valor}')