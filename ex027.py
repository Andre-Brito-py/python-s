idade = int(input('Quantos anos você tem? '))

if idade <= 9:
    print('Você está na categoria MIRIM')
elif 9 <= idade <= 14:
    print('Você está na categproa INFANTIL')
elif 14 <= idade <= 19:
    print('Você está na categoria JUNIOR')
elif 19 <= idade <= 20:
    print('Você está na categoria SÊNIOR')
elif idade > 20:
    print('Você é MASTER!')
