from random import randint
from time import sleep
jogadas = list()
jogos = list()

total_jogos = 1
quant = int(input('Quantas jogos quer que eu sorteie? '))
print()
print('-='*5, f' SORTEANDO {quant} JOGOS ', '=-'*5)
sleep(1.25)
while total_jogos <= quant:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in jogos: # para saber se um número está repetido
            jogos.append(num)
            cont += 1
        if cont >= 6:
            break
    jogos.sort()
    jogadas.append(jogos[:])
    jogos.clear()
    total_jogos += 1
for i, l in enumerate(jogadas):
    print(f'O jogo {i+1} foi: {l}')
    sleep(1.25)
print('\nESCOLHA UM JOGO E BOA SORTE')