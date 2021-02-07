print('Seja bem vindo! Nossa Carne está com 5% de desconto APROVEITE\n')

p1 = 'arroz'
p2 = 'feijão'
p3 = 'macarrão'
p4 = 'carne'

v1 = 4.0
v2 = 5.35
v3 = 2.25
v4 = 21.45

d1 = v1-v1*(5/100)
d2 = v2-v2*(5/100)
d3 = v3-v3*(5/100)
d4 = v4-v4*(5/100)

print('-'*30)
print('PRODUTOS')
print('-'*30)

print('{:2} --------{:2}'.format(p1, v1))
print('{:2} -------{:2}'.format(p2, v2))
print('{:2} -----{:2}'.format(p3, v3))
print('{:2} --------{:2}'.format(p4, v4))

print('-'*30)

compra =(input('Escolha um produto:\n'))

print('Você escolheu {}\n'.format(compra))

if compra == p4:
    print('Estamos com um desconto de 5% somente hoje\n\nCaso queira comprar o valor a ser pago será R${:.2f}\n\n'.format(d4))
#print('Estamos com um desconto de 5% somente hoje\nCaso queira comprar o valor a ser pago será {:.2f}'.format(d))
    print('Boas compras!')
elif compra == p1:
    print('O valor do {} é R${:.2f}\n\nPor favor se dirigir ao caixa\n'.format(p1, v1))
    print('Boas compras!')
elif compra == p2:
    print('O valor do {} é R${:.2f}\n\nPor favor se dirigir ao caixa\n'.format(p1, v2))
    print('Boas compras!')
elif compra == p3:
    print('O valor do {} é R${:.2f}\n\nPor favor se dirigir ao caixa\n'.format(p1, v3))
    print('Boas compras!')
else:
    print('Produto Inválido\n\nDigite o nome do produto corretamente')

