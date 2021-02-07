'''n1 = int(input('Digite um numero: ')) #jeito que eu fiz
n2 = int(input('Digite um numero: '))
n3 = int(input('Digite um número: '))
n4 = int(input('Digite um número: '))
lista = (n1, n2, n3, n4)
print('Os valores digitados foram:', end=' ')
for n in lista:
    print(n, end=' ')'''
#outra forma de fazer by guanabara
num = (int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')))
print(f'Os números que você digitou foram: {num}')
if 9 in num:
    print(f'O numero 9 foi digitado {num.count(9)} vezes')
else:
    print('O numero 9 não foi digitado')
if 3 in num:
    print(f'O numero 3 foi colocado na {num.index(3)+1}ª posição')
else:
    print('O numero 3 não foi colocado em nenhuma posição')
print(f'Os valores pares digitados foram: ',end='')
for par in num:
    if par % 2 == 0:
        print(par, end=' ')
    elif par % 2 == 1:
        print('0')
        break