n = cont = media = maior = menor = soma = 0
parar = ''
while parar in 'S, SIM':
    n = int(input('Digite um número: '))
    parar = str(input('você quer coninuar? ')).upper().strip()
    soma += n
    cont += 1
    media = float(soma/cont)
    if cont == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
print('A média dos {} valores digitados é {:.2f}'.format(cont, media))
print('O maior número digitado foi {} e o menor foi {}'.format(maior, menor))