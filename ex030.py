import random

junken = str(input('Hora do Jankenpo. Escolha pedra, papel, ou tesolra! '))
poh = random.choice (['pedra', 'papel', 'tesolra'])
 

if junken == 'papel' and poh == 'tesolra':
    print('O jogador teve o papel cortado pela tesolra do PC! Você perdeu')
elif junken == 'papel' and poh == 'papel':
        print('Ambos os jogadores escolheram papel! Empate!')
elif junken == 'papel' and poh == 'pedra':
        print('O papel do jogador envolveu a pedra do PC! Você venceu!')

elif junken == 'pedra' and poh == 'papel':
    print('O jogador teve sua pedra envolvida pelo papel do PC! Você perdeu!')
elif junken == 'pedra' and  poh == 'pedra':
        print('Ambos os jogadores escolheram pedra! Empate!')
elif junken == 'pedra' and poh == 'tesolra':
        print('A pedra do jogador esmagou a tesolra do PC! Você venceu!')

elif junken == 'tesolra' and poh == 'pedra':
    print('A tesolra do jogador foi esmagada pela pedra do PC! Você Perdeu!')
elif junken =='tesolra' and poh == 'tesolra':
        print('Ambos os jogadores escolheram tesolra! Empate!')
elif junken == 'tesolra' and poh == 'papel':
        print('A tesolra do jogador partiu ao meio a folha do PC! Você venceu!')