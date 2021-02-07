from random import randint
from time import sleep

num = 0
num_pc = randint(0,10)
cont_vezes = 1

print('<-=->'*14)
print('Estou pensando em um numero de 0 a 10 vamos ver se consegue acertar: ')
print('<-=->'*14)
print(num_pc)#resposta do num_pc para testar mudanças no programa
num = int(input('Faça sua jogada: '))
sleep(0.5)

while num != num_pc:
    num = int(input('Você errou tente novamente: '))
    cont_vezes += 1
    sleep(0.5)
print('\n'+'<-=->'*7)
print('''Você acertou!!!
Jogador escolheu {}
Computador escolheu {}'''.format(num, num_pc))
if cont_vezes == 1:
    print('Você acertou de primeira')
else:
    print('Você acertou depois de {} vezes'.format(cont_vezes))
print('<-=->' * 7)
