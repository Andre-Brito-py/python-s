valor = float(input('Qual o valor do produto? '))
pagamento = str(input('Qual o pagamento será a vista, ou no cartão? '))

if pagamento == 'a vista':
    forma = str(input('Qual vai ser o meio de pagamento, especie, cheque, ou cartão? '))
    if forma in ('especie', 'cheque'):
        final = valor - ((10 / 100) * valor)
        print('A forma de pagamento escolhida oferece 10% de desconto! O valor do seu produto fica {:.2f}' .format(final))

elif pagamento == 'cartão':
    forma = str(input('Será a vista, ou pretende dividir? '))
    if forma == 'a vista':
        final = valor - ((5 / 100) * valor)
        print('A forma de pagamento escolhida oferece 5% de desconto! O valor do seu produto fica {:.2f}' .format(final))
    elif forma == 'dividir':
        vezes = str(input('Em quantas vezes irá dividir? '))
        if vezes == 'duas vezes':
            final = valor / 2
            print('O valor do seu produto é de {}, e sai por duas parcelas de {}' .format(valor, final))
        else:
            final = valor + ((30 / 100) * valor)
        print('Como foi dividido em mais vezes, houve 30% de juros, e seu produto fica por {}' .format(final))