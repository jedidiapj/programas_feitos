# t = 'CONVERSOR DE MEDIDAS'
# print('{:=*20}'.format(t))
print('CONVERSOR DE MEDIDAS')
print('='*60)
medida = float(input('Digite uma distancia em metros:\n'))
cent = medida*100
mil = medida*1000

print('{} equivale à {} centimetros e {:.2f} milimetros'.format(medida, cent, mil))
