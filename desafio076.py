produtos = ('arroz', 2.75, 'chocolate', 5, 'biscoito', 3)
titulo = 'LISTA DE PRODUTOS'
print('~~'*15)
print(f'{titulo:^30}')
print('~~'*15)
for pos in range(0,6):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<20}', end='')
    else:
        print(f'R${produtos[pos]:>7.2f}')
print('~~'*15,end='')