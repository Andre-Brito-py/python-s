salario = float(input('Qual o seu lalário atual? R$ '))

if salario <= 1250:
    aumento_1 = float(salario * (10 / 100) + salario)
    print('Seu sálario aumentou para R$ {:.2f}' .format(aumento_1))

else:
    aumento_2 = float(salario * (15 / 100) + salario)
    print('Seu salario aumentou para R# {:.2f}' .format(aumento_2))