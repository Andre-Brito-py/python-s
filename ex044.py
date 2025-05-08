from random import randint

print('-=' * 25)
print('VAMOS JOGAR PAR OU IMPAR')
print('-=' * 25)

vitorias = 0

while True:
    jogador = int(input('Digite um valor: '))
    while jogador > 5 or jogador < 0:
        print('Você só tem cinco dedos... tente novamente!')
        jogador = int(input('Digite um valor: '))
    escolha = str(input('Você quer par ou impar? [P/I]: ')) .upper() .strip()
    computador = randint(1, 5)
    soma = jogador + computador
    
    
    if (soma % 2 == 0 and escolha == 'P') or (soma % 2 == 1 and escolha == 'I'):
        print(f'Você escolheu {jogador} e o computador escolheu {computador}, a soma é {soma}.\nVocê Venceu!\n')
        print('=-' * 15)
        vitorias += 1

    else:
        print(f'Você escolheu {jogador} e o computador escolheu {computador}, a soma é {soma}.Você perdeu!\n')
        break
    
print('-' * 25)
print(f'\nGAME OVER! Você venceu {vitorias} vez(es).')
  
