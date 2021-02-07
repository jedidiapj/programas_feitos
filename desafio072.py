numeros = ('zero','um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatoze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
n = 0
while True:
    n = int(input('Digite um numero entre 0 e 20: '))
    if n >= 0 and n <= 20:
        '''for pos, cont in enumerate(numeros):# minha forma complicada de fazer
            if pos == n:
                print(numeros[pos])'''
        break
    else:
        print('Você digitou um numero errado. tente novamente')
        continue
print(f'voce digitou o número {numeros[n]}') #forma do guanabara