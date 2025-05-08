#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por Km rodado.

k = float(input('Quantos km foram percorridos com o carro? '))
d = int(input('Por quantos dias o carro foi alugado? '))
c = float(60 * d)
r = float(0.15 * k)
v = float(c + r)
print('O valor a se pagar pela quantidade de dias é R${:.2f}, mais o extra por km rodado é de R${:.2f}, sendo assim, o valor total a ser pago é R${:.2f}' .format(c, r, v))