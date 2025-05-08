# Lê um número inteiro digitado pelo usuário
n = int(input('Digite um número inteiro: '))

# Começa assumindo que o número é primo
eh_primo = True

# Números menores que 2 não são primos (0 e 1, por exemplo)
if n < 2:
    eh_primo = False
else:
    # Testa se n é divisível por algum número entre 2 e n-1
    for i in range(2, n):
        # Se for divisível, então NÃO é primo
        if n % i == 0:
            eh_primo = False
            break  # Já sabemos que não é primo, então podemos parar o laço

# Mostra o resultado baseado na variável eh_primo
if eh_primo:
    print('Esse é um número primo.')
else:
    print('Esse não é um número primo.')