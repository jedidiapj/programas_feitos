p1 = int(input('Quantos dias o carro foi alugado? '))
p2 = float(input('Quantos KM rodou?'))

dias = p1*60
km = p2*0.15
total = dias+km

print('O total a pagar é R${:.2f}'.format(total))
