import math

#Entrada
angulo_graus = float(input('Digite o valor do âgulo em graus: '))

#Cauculo
#Conversão para radianos:
angulo_radianos = math.radians(angulo_graus)
#Cauculo das funções trignometricas
seno = math.sin(angulo_radianos)
cosseno = math.cos(angulo_radianos)
tangente = math.tan(angulo_radianos)

#Saida
print('O seno do âgulo é {:.2f}°; \nO cosseno é {:.2f}°; \nE a tangente é {:.2f}°.' .format(seno, cosseno, tangente))