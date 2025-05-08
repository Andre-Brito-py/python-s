n = cout = total = 0

while True:
    n = int(input('Digite um valor (999 faz parar): '))
    if n == 999:
        break
    cout += 1
    total += n
     
print(f'a soma dos {cout} valores é {total}')