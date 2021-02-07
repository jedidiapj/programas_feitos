dist_viagem = float(input('Qual é a distancia da viagem?\n'))
passagem1 = dist_viagem*0.5
passagem2 = (dist_viagem-200)*0.45

if dist_viagem >= 200:
    print('O valor da passagem é: R${:.2f}'.format(passagem1))
else:
    print('O valor da passagem é: R${:.2f}'.format(passagem2))