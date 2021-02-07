p = int(input('Digite o 1º termo: '))
r = int(input('Digite a razão: '))
t = int(input('Quantos termos você quer mostrar? '))
termo = p
cont = 1
q = t
total = 0
while q != 0:
    total += q
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += r
        cont += 1
    print('PAUSA')
    q = int(input('\nVocê gostaria de mostrar mais termos? '))
print('progressao finalizada com {} termos'.format(total))
