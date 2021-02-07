from random import randint
from time import sleep # faz o computador realizar delay antes da próxima função

print('-=-'*20)
print('Estou pensando em um número de 0 a 5')
print('-=-'*20)
numero = int(input('Que numero eu pensei?\n'))
numero_pc = randint(0,5)

print('PROCESSANDO...')
sleep(1.5)
print('O número escolhido foi {}\n'.format(numero_pc))
if numero == numero_pc:
    print('Parabens vc acertou')
else:
    print('Você perdeu, Tente novamente')