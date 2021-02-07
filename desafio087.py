matriz = [[[], [], []], [[], [], []], [[], [], []]]
soma_par = soma_3 = maior_2 = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um número para a posição [{l},{c}]: '))
        if matriz[l][c] % 2 == 0:
            soma_par += matriz[l][c]
        if c == 2:
            soma_3 += matriz[l][c]
        if l == 1:
            maior_2 = matriz[l][c]
        elif l > maior_2:
            maior_2 = matriz[l][c]


for l in range(0, 3):
    for c in range(0,3):
        print(f'[{matriz[l][c]}]', end='')
    print()

print(f'A soma de todos os pares é: {soma_par}')
print(f'A soma da 3 coluna é: {soma_3}')
print(f'O maior valor da 2 linha é: {maior_2}')
