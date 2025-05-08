n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
n3 = int(input('Último numero: '))

maior = max(n1, n2, n3)
menor = min(n1, n2, n3)

print('{} é o maior número! \nE o menor número é {}!' .format(maior, menor))