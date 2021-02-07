velo_carro = float(input('Diga sua velocidade atual:\n'))
multa = (velo_carro-80)*7

if velo_carro <= 80:
    print('Dirija sempre com segurança')
else:
    print('''Você foi multado por exesso de velocidade'
Sua multa é no valor de R${:.2f}'''.format(multa))