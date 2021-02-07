import random
num = soma = jogada_pc = cont = 0
jogo = par = impar = ''
titulo = 'VAMOS JOGAR TABUADA'
print('~~'*15)
print(f'\033[1;033m      {titulo:^20}\033[m')
print('~~'*15)
while True:
    num = int(input('Escolha um número:'))
    jogo = str(input('PAR OU IMPAR? ')).upper().strip()
    jogada_pc = random.randint(0,10)
    soma = (num + jogada_pc) % 2
    print('--'*15)
#reconhece se o numero é par ou impar
    if jogo in 'PAR,IMPAR':
        if soma == 0:
            par = 'PAR'
            print(f'Você escolheu {num} e o computador {jogada_pc}. Resultado {num + jogada_pc} é {par}')
            print('--' * 15)
        elif soma == 1:
            impar = 'IMPAR'
            print(f'Você escolheu {num} e o computador {jogada_pc}. Resultado {num+jogada_pc} é {impar}')
            print('--' * 15)
#lê as jogadas e define quem ganhou
        if jogo == 'PAR' and soma == 0:
            print('Você ganhou')
            print('-=-'*10)
        elif jogo == 'PAR' and soma == 1:
            print('Você perdeu')
            print('-=-' * 10)
            ree_play = str(input('Gostaria de jogar novamente? ')).upper().strip()
            if ree_play in 'S,SIM':
                continue
            break
        elif jogo == 'IMPAR' and soma == 1:
            print('Você ganhou')
            print('-=-' * 10)
        elif jogo == 'IMPAR' and soma == 0:
            print('Você perdeu')
            print('-=-' * 10)
            ree_play = str(input('Gostaria de jogar novamente? ')).upper().strip()
            if ree_play in 'S,SIM':
                continue
            break
        cont += 1
    else:
        print('jogada inválido tente novamente')
print(f'\nGAME OVER. Você ganhou {cont} vezes')
print('\nOBRIGADO POR JOGAR\n')

