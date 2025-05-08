soma = 0
cont = 0

for _ in range(6):
    n = int(input('Digite um numero: '))
    if n % 2 == 0:
        soma += n
        cont += 1
        
print('VocÊ informou {} numeros pares, e a soma deles é {}' .format(cont, soma))