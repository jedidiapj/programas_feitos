from time import sleep
num1 = 0
num2 = 0
num_maior = 0
opcao = 0
opcao2 = ''

for c in range(1, 3):
    num = float(input('Digite o {}º numero: '.format(c)))
    if c == 1:
        num1 = num
    else:
        num2 = num
while opcao != 5:

    print('\n' + '-+-' * 10)
    print('''         MENU:
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA''')
    print('-+-' * 10)
    opcao = int(input('ESCOLHA UMA DAS OPERAÇÕES: '))
    print('-+-' * 10)

    if opcao == 1:
        print('\n{} + {} = {}'.format(num1, num2, (num1+num2)))
        print('\n' + '-+-' * 10)
        opcao2 = str(input('\nDeseja voltar para o menu: ')).upper()
        if opcao2 in 'S,SIM':
            continue
        else:
            break
    elif opcao == 2:
        print('\n{} x {} = {}'.format(num1, num2, (num1*num2)))
        print('\n' + '-+-' * 10)
        opcao2 = str(input('\nDeseja voltar para o menu: ')).upper()
        if opcao2 in 'S,SIM':
            continue
        else:
            break
    elif opcao == 3:
        if num1 > num2:
            num_maior = num1
            print(f'\nO número maior é {num_maior}')#usando f'string
        elif num1 < num2:
            num_maior = num2
            print('\nO número maior é {}'.format(num_maior))
        else:
            print('\nOs numeros são iguais')
            print('\n' + '-+-' * 10)
        opcao2 = str(input('\nDeseja voltar para o menu: ')).upper()
        if opcao2 in 'S,SIM':
            continue
        else:
            break
    elif opcao == 4:
        print('Informe os novos números:\n')
        for c in range(1, 3):
            num = float(input('''Digite o {}º número: '''.format(c)))
            if c == 1:
                num1 = num
            else:
                num2 = num
    elif opcao != 5:
        print('\nEscolha uma opção válida:')
        #opcao = opcao aqui não foi nessário pois não houve outra interação com o usuário
    sleep(1.25)# ao fim de cada proposição adiciona um delay
print('\nObrigado por usar nosso programa')
