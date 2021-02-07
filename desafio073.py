times = ('São Paulo', 'Internacional', 'Atlético-MG', 'Flamengo',
         'Grêmio', 'Palmeiras', 'Fluminense', 'Santos', 'Ceará',
         'Corinthians', 'Athletico', 'Atlético-GO',
         'Red Bull Bragantino', 'Sport', 'Vasco',
         'Fortaleza', 'Bahia', 'Goiás', 'Botafogo', 'Curitiba')
titulo = 'CAMPEONATO BRASILEIRO'
op = 0
nome = ''

print('\033[034m=\033[m'*31)
print(f'\033[1;032m{titulo:^31}\033[m')
while True:
    print('\033[032m=\033[m' * 31)
    print('''\033[034m[1]\033[m os 5 primeros times
\033[032m[2]\033[m os 4 ultimos times
\033[034m[3]\033[m localize time
\033[032m[4]\033[m tabela em ordem alfabética
\033[034m[5]\033[m fim''')
    print('\033[034m=\033[m' * 31)
    op = int(input('Escolha uma opção: '))
    if op == 1:
        print(times[:5])
    elif op == 2:
        print(times[16:])
    elif op == 3:
        nome = str(input('Digite o nome de um time: ')).title()
        if nome in times:
            print(f'O time {nome} está na {times.index(nome) + 1}ª posição')
        else:
            print('digite o nome de um time válido')
    elif op == 4:
        print(sorted(times))
    elif op == 5:
        print('obrigado por usar nosso programa')
        break
    else:
        print('Escolha uma opção correta')


