#Crie um programa que leia o nome completo de uma pessoa e mostre: o nome com todas as letras maiúsculas, o nome com todas as letras minúsculas, quantas letras tem ao todo (sem considerar espaços), quantas letras tem o primeiro nome.

#Entrada
nome = input('Digite seu nome completo: ').strip()

#Cauculo
#Transforma as letras em maúsculas:
print('Nome com todas as letras maúsculas: {}' .format(nome).upper())
#Transforma todas as letras em minusculas:
print('Nome com todas as letras minúsculas: {}' .format(nome).lower())
#Conte as letras:
letras = len(nome.replace('','')) #OBS: replace(" ", "") cria uma nova string, removendo todos os espaços. len(...) retorna o número de caracteres dessa nova string.
print('Quantidade de letras no nome: {}' .format(letras))
#Conta as letras do primeiro nome:
primeiro_nome = nome.split()[0]
print('Quantidade de letras no primeiro nome:{}' .format(len(primeiro_nome)))
#.split() separa a string em partes, usando o espaço como separador:"Maria Clara" vira ["Maria", "Clara"].
#[0] acessa o primeiro elemento da lista, ou seja, o primeiro nome.
#len(...) conta quantas letras tem esse primeiro nome.
