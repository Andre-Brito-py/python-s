from random import randint
from time import sleep
from operator import itemgetter

jogo = {'jogador_1': randint(1, 6),
        'jogador_2': randint(1, 6),
        'jogador_3': randint(1, 6),
        'jogador_4': randint(1, 6)
}


print('OS VALORES SORTEADOS FORAM...')
print('=-' * 30)

ranking = sorted(jogo.items(), key = itemgetter(1))

for chave, valor in jogo.items():
    print(f'{chave} tirou {valor} no dado')
    sleep(1)