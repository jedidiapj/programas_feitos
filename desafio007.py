nota1 = float(input('Digite a primeira nota:\n'))
nota2 = float(input('Digite a segunda nota:\n'))

media = (nota1+nota2)/2

print('Sua média foi: {}\n'.format(media))

if media >= 7:
    print('Parabéns Você Passou')
else:
    print('Você ficou de recuperação!\nPrecisa estudar mais')
