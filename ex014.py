#Faça um programa que leia um numero de 0 a 9999, e mostre na tela os dados digitos separados. Ex: 1854. unidade: 4; dezena: 3; centena: 8; milhar: 1

#Entrada
numero = int(input('Digite um numero de 1 a 9999: '))

#Cauculo
unidade = numero % 10
dezena = (numero // 10) % 10
centena = (numero // 100) % 10
milhar = (numero // 1000) % 10

#Saida
print('Unidade:', unidade)
print('Dezena:', dezena)
print('Centena:', centena)
print('Milhar:', milhar)