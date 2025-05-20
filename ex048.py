times_pro_demaix = ('Dragões de Aço', 'Falcões Noturnos', 'Lobos do Norte',
                     'Titãs de Fogo', 'Serpentes Negras', 'Guardiões do Vale', 'Leões de Prata', 'Trovões do Oeste', 'Corvos de Gelo', 'Guerreiros da Tempestade')

posicao = times_pro_demaix.index('Corvos de Gelo')


print(f'Os cinco primeiros são {times_pro_demaix[0:5]}')
print(f'Os últimso quatro são {times_pro_demaix[6:]}')
print(f'A posição do time {times_pro_demaix[8]} é {posicao + 1}')