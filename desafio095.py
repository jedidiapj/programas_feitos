stats = list()
jogadores = dict()
gol_jogos = list()
print('*' * 30)
while True:
    jogadores['Nome'] = str(input('Nome jogador: '))
    partidas = int(input('Quantas partidas jogou? '))

    for j in range(partidas):
        gol_jogos.append(int(input(f'Quantos gols no jogo {j+1}: ')))
    jogadores['gols'] = gol_jogos[:]
    jogadores['Total gols'] = sum(gol_jogos)
    gol_jogos.clear()
    stats.append(jogadores.copy())
    sair = str(input('Deseja continuar? [S/N] ')).upper().strip()
    print('*' * 30)
    if sair in 'S,SIM':
        continue
    else:
        break
print('-'*40)
print('cod ', end='')
for i in jogadores.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for i, v in enumerate(stats):
    print(f'{i:>3} ',end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)
while True:
    opcao = int(input('Mostrar dados de qual jogador? '))
    if opcao == 999:
        break
    if opcao >= len(stats):
        print('Escolha um código correto')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {stats[opcao]["Nome"]}')
        for i, g in enumerate(stats[opcao]['gols']):
            print(f'No jogo {i + 1} fez {g} gols')