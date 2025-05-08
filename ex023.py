valor_da_casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu sálario? R$'))
anos = int(input('Em quantos anos pretende pagar a casa? '))
parcela = valor_da_casa / (anos * 12)
if parcela <= (salario * 30) / 100:
    print('Parabéns, seu financiamento foi aprovado! ✅ \nSuas parcelas são de R${:.2f}' .format(parcela))
else:
    print('Infelizmente, seu finaiciamento não foi aprovado ❌')