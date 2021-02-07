maior = 0
menor = 0
for p in range(1,6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi {} e o menor foi {}'.format(maior, menor))

#outra forma de fazer
'''lista = []
for c in range(1,6):
    lista.append(float(input('Digite o peso da {}ª pessoa: '.format(c))))#adiciona o imput em uma lista
    p_maior = max(lista)
    p_menor = min(lista)
print('O maior peso lido foi de {}'.format(p_maior))
print('O menor peso lido foi de {}'.format(p_menor))'''
