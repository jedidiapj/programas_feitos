from time import sleep


def contador():
    print('<>' * 15)
    print('Contagem de 1 até 10 de 1 em 1')
    for n in range(1, 11):
        print(n, end=' ')
        sleep(0.25)
    print('FIM')
    print('<>' * 15)
    print('Contagem de 10 até 0 de 2 em 2')
    for n in range(10, -1, -2):
        print(n, end=' ')
        sleep(0.25)
    print('FIM')


def contador2(i, f, p):
    print(f'Contagem de {i} até {f} de {p} em {p}')


#programa principal
contador()
while True:
    print('<>' * 15)
    print('Agora é sua vez de personalizar a contagem')
    i = int(input('Início: '))
    f = int(input('Fim: '))
    p = int(input('Passo: '))

    if i < f:
        if p == 0:
            p = 1
        contador2(i,f,p)
        for n in range(i, f+1, p):
            print(n, end=' ')
            sleep(0.25)
        print('FIM')
    if i > f:
        if p == 0:
            p = 1
        contador2(i, f, p)
        for n in range(i, f-1, -p):
            print(n, end=' ')
            sleep(0.25)
        print('FIM')

    while True:
        opcao = str(input('Deseja continuar? [S/N] ')).upper().strip()
        if opcao in 'S,SIM':
            break
        if opcao not in 'S,SIM,N,NAO,NÃO':
            print('Responda com S ou N')
            continue
        else:
            break
    if opcao in 'S,SIM':
        continue
    if opcao in 'N,NAO,NÃO':
        break
