import math

#Entrada
cateto_oposto = float(input('DIgite o valor do cateto oposto '))
cateto_adjacente = float(input('Digite o calor do cateto adjacente '))

#cauculo
hipotenusa = math.sqrt(cateto_oposto ** 2 + cateto_adjacente ** 2)

#saida
print('A hipotenusa do triangulo é {:.2f}' .format(hipotenusa))