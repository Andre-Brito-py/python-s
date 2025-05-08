#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"

# Lê o nome da cidade e remove espaços antes e depois
cidade = input("Digite o nome de uma cidade: ").strip()

# Verifica se começa com "Santo", ignorando letras maiúsculas ou minúsculas
comeca_com_santo = cidade.lower().startswith("santo")

# Mostra o resultado
if comeca_com_santo:
    print("A cidade começa com 'Santo'.")
else:
    print("A cidade NÃO começa com 'Santo'.")
