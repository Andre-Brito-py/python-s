#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
a = input('Digite algo: ')
print('O tipo primitivo do valor é: ' , type(a))
print('Só tem espaços?' , a.isspace())
print('Só tem numeros?' , a.isnumeric())
print('Só tem letras?' , a.isalpha())
print('Tem números e/ou letras?' , a.isalnum())
