ano = int(input('Digite o ano que quer consultar: '))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print('O ano que você digitou é bisexto! ✅')
else:
   print('O ano que você digitou não é bixesto! ❌')

