cadastro = list()
pessoas = dict()
idade = list()
while True:
    pessoas.clear()
    pessoas['Nome'] = str(input('Nome: '))
    pessoas['Idade'] = int(input('Idade: '))
    while True:
        pessoas['Sexo'] = str(input('Sexo [M/F]')).upper().strip()[0]
        if pessoas['Sexo'] in 'MF':
            break
        print('Erro! Por Favor, digite apenas M ou F')
    cadastro.append(pessoas.copy())
    idade.append(pessoas['Idade'])
    sair = str(input('Deseja continuar? [S/N]')).upper().strip()
    if sair in 'S,SIM':
        continue
    else:
        break
media = sum(idade)/len(cadastro)
print(cadastro)
print(f'- O grupo tem {len(cadastro)} pessoas')
print(f'- A média de idade é de {media:.2f}')
print('- As mulheres cadastradas foram: ', end='')
for s in cadastro:
    if s['Sexo'] == 'F':
        print(s['Nome'], end=' ')
print()
print('- Lista de pessoas que estão acima da média:\n')
for i in cadastro:
    if i['Idade'] >= media:
        for k, v in i.items():
            print(f'{k} = {v}', end=' ')
        print()
print('\nTHE END')
