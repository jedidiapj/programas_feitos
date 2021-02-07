def fatorial(a, b=False):
    '''
    -> Faz o fatorial de um número
    :param a: Faz o fatorial do número
    :param b: (opcional) Mostra ou não a conta
    :return: retorna o fatorial
    '''

    f = 1
    for c in range(a, 0, -1):
        f *= c
        if b == True:
            print(f'{c}', end=' ')
            if c > 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
    return f


while True:
    n = int(input('Digite um número para saber seu fatorial: '))
    m = str(input('Devo mostrar a conta? ')).upper()
    if m not in 'N,NÃO,NAO':
        f1 = fatorial(n, True)
        print(f1)
    else:
        f1 = fatorial(n)
        print(f1)
    sair = str(input('Deseja continuar: ')).upper()
    if sair not in 'N,NÃO,NAO':
        continue
    else:
        print('Obrigado por usar nosso programa')
        break

