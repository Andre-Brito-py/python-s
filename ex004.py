n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
sub = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {} \n a multiplicação é {} a divisião é {:.3f}'.format(s, m, d)) 
#na divisão, foi adicionado :.3 dentro das chaves {}, para que houvem no máxom três numeros depois da virgula.
#\n serve para quebrar a linha
print('A divisão inteira é {}, a exponeciação é {}, a subtração é{}'.format(di, e, sub))
