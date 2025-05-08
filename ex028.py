altura = float(input('Qual a sua altura? '))
peso = float(input('Qual o seu peso? '))
imc = peso / (altura * 2)

if imc < 18.5:
    print('Seu IMC é de {:.2f}, está a baixo do peso, precisa se alimentar melhor!' .format(imc))

elif 18.5 < imc <= 25:
    print('Seu IMC é de {:.2f}, parabéns! Você está em seu peso ideial' .format(imc))

elif 25 < imc <= 30:
    print('Seu IMC é {:.2f}, você está com um sobrepeso, ein...' .format(imc))

elif 30 < imc <= 40:
    print('Seu IMC é de {:.2f}, e, como você bem sabe, está obeso' .format(imc))

elif imc > 40:
    print('Seu IMC é de {:.2f}, e... bom, como você consegue ficar de pé?' .format(imc))