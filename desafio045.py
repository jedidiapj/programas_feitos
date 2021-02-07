from random import randint
from time import sleep
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0,2)

print ('''Escolha.....
[ 0 ] pedra
[ 1 ] papel
[ 2 ] tesoura''')
jogador = int(input('Faça sua jogada: '))
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('-=-'*11)
print('Jogador jogou {}'.format(itens[jogador]))
print('Computador jogou {}'.format(itens[computador]))
print('-=-'*11)

if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print("PC WIN")
    elif jogador == 2:
        print('Você venceu')
    else:
        print('Jogada inválida')
elif computador == 1:
    if jogador == 0:
        print('PC WIN')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print("VOCÊ GANHOU")
    else:
        print('Jogada inválida')
elif computador == 2:
    if jogador == 0:
        print('VOCÊ GANHOU')
    elif jogador == 1:
        print('PC WIN')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada inválida')
