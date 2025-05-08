import random

#Entrada
nomes = [
input('Digite o primeiro nome: '),
input('Digite o segundo nome: '),
input('Digite o terceiro nome: '),
input('Digite o quarto nome: '),
]

#Cauculo
n_s = random.choice(nomes)

#Saída
print('O aluno azarado é: {}' .format(n_s))