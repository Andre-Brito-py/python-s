import random

j = int(input('Chute o numero que estou pensando e tente adivinhar qual é! '))
n = random.randint(1, 5)
if n == j:
    print('Você adivinhou! \n----O jogador venceu!----')
if j > 5:
    print('Você está realmente tentando jogar...?')
else:
    print('Você errou! \n----O computador venceu!----')
