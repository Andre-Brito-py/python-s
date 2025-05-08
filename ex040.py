import random

j = 0
n = random.randint(1, 10)
k = 0


while j != n:
    j = int(input('Chute o numero que estou pensando e tente adivinhar qual é! '))
    k =+ n
    if n == j:
        print('Você adivinhou depois de {} tentativas! \n----O jogador venceu!----' .format(k))
    elif j >= 11:
        print('Você está realmente tentando jogar...?')
