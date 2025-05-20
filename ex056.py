from time import sleep
from random import randint

print('JOGA NA MEGA SENA')
print('-' * 30)

quantidade = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=-=-  SORTEANDO {quantidade} JOGOS  -=-=-')

mega = []

for i in range(quantidade):
    jogo = []
    while len(jogo) < 6:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
    jogo.sort()
    mega.append(jogo[:])
    print(f'Jogo {i + 1}: {jogo}')
    sleep(1)  # pausa de 1 segundo entre os jogos

print('-=-=-= < BOA SORTE! > =-=-=-')

#fazer revisão