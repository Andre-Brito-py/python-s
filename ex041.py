n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

r = 0

while r != 5:
    soma = n1 + n2
    multiplicar = n1 * n2
    maior = max(n1, n2)


    r = int(input('Escolha uma das opções: \n[1] para somar \n[2] para multiplicar \n[3] para mostrar o maior numero \n[4] se você digita mudar os numeros \n[5] SAIR \n'))


    if r == 1:
        print('A soma dos dois valores é: {}' .format(soma))
    elif r == 2:
        print('A multiplicação entre os dois números é: {}' .format(multiplicar))
    elif r == 3:
        print('O maior número entre os dois valores é {}' .format(maior))
    elif r == 4:
        n1 = int(input('Digite um novo valor: '))
        n2 = int(input('Digite outro novo valor: '))
    elif r == 5:
        print('FIM')
    else:
        print('Opção invalida, tente novamente')