peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso/altura**2

print('O seu IMC é: {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso')
elif imc < 25:
    print('Você está no seu peso ideal')
elif imc <= 30:
    print('Você está com sobrepeso')
elif imc <= 40:
    print('Você está com obesidade')
else:
    print('Você está com obesidade mórbida')