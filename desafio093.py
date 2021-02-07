jogador = dict()
gol_jogos = list()

print('*'*20)
jogador['Nome'] = str(input('Nome do jogador: '))
partidas = int(input('Quantas partidas foram jogadas? '))

for j in range(partidas):
    gol_jogos.append(int(input(f'quantos gols na {j+1} partida? ')))
jogador['gols'] = gol_jogos[:]
jogador['Total'] = sum(gol_jogos)
print('*'*20)
print(jogador)
print('*'*20)

for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')
print('*'*20)
print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas')

for j in range(partidas):
    print(f'    => Na partida {j + 1} fez {gol_jogos[j]} gols')
print(f'Foi um total de {jogador["Total"]} gols.')

