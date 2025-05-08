idade = int(input('DIgite a sua idade, cidadão: '))

if idade < 18:
    falta = int(18 - idade)
    print('Ainda não está na hora, cidadão, faltam {} anos para se apresentar ao exercíto' .format(falta))

elif idade == 18:
    print('Parabéns, cidadão, digo, soldado! chegou o momento de servir a sua pátria capinando mato e pintando paredes!')

elif idade > 18:
    passou = int(idade - 18)
    print('Estavámos a sua espera a {} anos, soldado, bem-vindo ao lar. Ali está a sua inchada e o seu pincel' .format(passou))