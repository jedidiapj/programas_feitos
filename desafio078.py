valores = []
for cont in range(0, 5):
    valores.append(int(input(f'Digite o {cont+1}º valor: ')))
print(f'O maior valor foi {max(valores)} na posição: ', end='')
for p, v in enumerate(valores):
    if v == max(valores):
        print(f'{p}...', end='')
print(f'\nO menor valor foi {min(valores)} na posição: ', end='')
for p, v in enumerate(valores):
    if v == min(valores):
        print(f'{p}...', end='')
