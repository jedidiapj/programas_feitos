from random import randint
num = (randint(0, 10),randint(0, 10), randint(0, 10),
       randint(0, 10), randint(0, 10), randint(0, 10))
print('foram sorteados ')
for n in num:
    print(f'{n} ', end='')

print(f'\nO maior valor foi {max(num)}')
print(f'O menor valor foi {min(num)}')
