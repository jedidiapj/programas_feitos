r1 = float(input('Digite um número: '))
r2 = float(input('Digite um número: '))
r3 = float(input('Digite um número: '))

if r1 + r2 > r3:
    if r1 == r2 == r3:
        print('Triangulo Equilátero')
    elif r1 == r2 or r2 == r3 or r1 == r3:
        print('Triangulo isosceles')
    elif r1 != r2 != r3 != r1:
        print('Triandulo escaleno')
else:
    print('Valores não formam um triangulo')
