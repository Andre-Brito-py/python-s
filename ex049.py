from random import sample

r = sample (range(1, 101), 5)
n = (sorted(r))

print(f'Os numeros escolhidos foram {r}')
print(f'O maior valor é {n[-1]} enquanto o menor valor é {n[0]}')