from random import randint
from time import sleep
from operator import itemgetter
jogadas = {}
ranking = []

jogadas['jogador1'] = randint(1,7)
jogadas['jogador2'] = randint(1,7)
jogadas['jogador3'] = randint(1,7)
jogadas['jogador4'] = randint(1,7)

for k, v in jogadas.items():
    print(f'O {k} tirou {v}')
    sleep(1)

ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)
print()
for i, v in enumerate(ranking):
    print(f'{i+1} lugar: foi {v[0]} com {v[1]} ')
    sleep(1)

