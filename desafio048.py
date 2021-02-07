soma = 0
cont = 0

print('''Escolha um número para saber quantos multiplos ele tem entre 1 e 500 e a soma deles''')
escolha = int(input(''))

if escolha % 2 == 0:
    print('Você escolheu o numero {} que é PAR\n'.format(escolha))
    for bunda in range(0, 501, 2):
        if bunda % escolha == 0:
            soma += bunda
            cont = cont + 1
    print('A soma de todos os {} multiplos de {}  é {}'.format(cont-1, escolha, soma))
elif escolha % 2 != 0:
    print('Você escolheu os numero {} que é IMPAR\n'.format(escolha))
    for cu in range(1, 501, 2):
        if cu % escolha == 0:
            soma += cu
            cont = cont + 1
    print('A soma de todos os {} multiplos de {} é {}'.format(cont, escolha, soma))
else:
    print('Opção inválida')