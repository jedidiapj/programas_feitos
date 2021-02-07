from random import randint
from time import sleep

num = []
num_ordem = []

def maior(num):
    for v in range(0,3):
        for v in range(0, 5):
            n = randint(0, 100)
            if n not in num:
                num.append(n)
                num_ordem = sorted(num[:])
        print('-='*30)
        print('Analisando os valores passados')
        for n in num_ordem:
            print(f'{n}', end=' ')
            sleep(0.5)
        print(f'Foram informados {len(num_ordem)} ao todo')
        print(f'O maior o número informado foi {max(num_ordem)}')
        num.clear()
        num_ordem.clear()



'''for v in range(0,6):
    n = randint(0,6)
    if n not in num:
        num.append(n)'''
maior(num)
print('-='*30)