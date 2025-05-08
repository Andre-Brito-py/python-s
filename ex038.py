m = 0
r = 'S'
n = 0
par = impar = 0

while r == 'S': 
        n = int(input('Digite um valor: ')) 
        r = str(input('Quer continuar? [S/N] ')) .upper() .strip()
        m += n
        if n != 0:
            if n % 2 == 0:
                    par += 1
            else:
                    impar += 1
print('Você digitou {} numeros pares e {} numeros impares, e a soma de todos os valores são iguais a {}' .format(par, impar, m))
