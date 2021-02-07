from random import randint

num = list()


def sorteio(num):
    print('SORTEANDO 5 VALORES', end=' ')
    for v in range(0, 5):
        n = randint(0, 11)
        num.append(n)
        print(f'{n}', end=' ', flush=True)
    print()


def somar(num):
    soma = 0
    for v in num:
        if v % 2 == 0:
            soma += v
    print(f'Somando os valores pares de {num} temos {soma}', flush=True)


sorteio(num)
somar(num)