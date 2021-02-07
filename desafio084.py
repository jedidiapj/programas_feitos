pessoa = []
backup = []
maiorp = menorp = 0
while True:
    backup.append(str(input('Nome: ')))
    backup.append(int(input('Peso: ')))
    if len(pessoa) == 0:
        maiorp = menorp = backup[1]
    else:
        if backup[1] > maiorp:
            maiorp = backup[1]
        if backup[1] < menorp:
            menorp = backup[1]
    pessoa.append(backup[:])
    backup.clear()
    opcao = str(input('Deseja continuar? [S/N]')).upper().strip()
    if opcao in 'S/SIM':
        continue
    else:
        break
print(f'Foram cadastradas {len(pessoa)} pessoas')
print(f'O maior peso foi de {maiorp}Kg: ', end='')
for p in pessoa:
    if p[1] == maiorp:
        print(f'{p[0]}', end=' ')
print(f'\nO menor peso foi de {menorp}Kg: ', end='')
for p in pessoa:
    if p[1] == menorp:
        print(f'{p[0]}', end=' ')
print(pessoa)