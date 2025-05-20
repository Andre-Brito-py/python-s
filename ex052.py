valores = []

while len(valores) < 5:
    numero = int(input('Digite um valor: '))
    if numero in valores:
        print('Valor duplicado! tente novamente')
    else:
        valores.append(numero)
        print('Valor adicionado com sucesso')
    
    print(f'Os valores adicionados foram {sorted(valores)}')
