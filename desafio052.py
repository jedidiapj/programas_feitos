num = int(input('Digite um número: '))
tot = 0

for c in range(1, num+1):#se utiliza num+1 pois no python o range sempre desconsidera o ultimo número/ num+1 pois queremos que o programa chegue até o numero informado
    if num % c == 0: #teste para saber quais e quantos numeros são multiplos de num
        print('\33[33m ', end = '')#destaca os multiplos
        tot += 1 #se o numero for divisivel é +1 no total por isso tot = 0
    else:
        print('\033[31m ', end= '')#destaca os não multiplos
    print('{}'.format(c), end='')#mostra os números de for em sequencia
print('\n\033[mO número {} foi divisivel {} vezes'.format(num, tot))#apresenta o resultado da condição
if tot == 2:#para ser primo o numero deve ser apenas divisivel por 1 e por ele mesmo
    print('E por isso ele é PRIMO')
else:
    print('E por isso ele não é PRIMO')
