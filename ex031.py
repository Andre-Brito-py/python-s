import time

n = str(input('Digite "começar" para iniciar a contagem! '))
if n == 'começar':
    print('Vamos para contagem do ano novo!!!')
    time.sleep(1)
    for c in range(10, 0, -1):
        print(c)
        time.sleep(1)
    print('FELIZ ANO NOVO!!! 🥂 🎆')