nota_um = float(input('Digite a primeira nota: '))
nota_dois = float(input('Digite a segunda nota: '))
media = (nota_um + nota_dois) / 2

if media < 5:
    print('Sua média é {}, reprovado, filhão' .format(media))


elif 5 <= media <= 6.9:
    print('Sua média é {}, ficou de recuperação, ótario' .format(media))
    

elif media >= 7:
    print('Sua média é {}, ou seja, você passou, parabéns!' .format(media))