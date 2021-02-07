from math import hypot

co = float(input('Digite o comprimeto do Cateto Oposto: '))
ca = float(input('Digite o comprimento do Cateto Adjacente: '))
hp = hypot(co, ca)

print('A hipotenusa é {:.2f}'.format(hp))