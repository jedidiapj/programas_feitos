total = totmil = p_barato = cont = 0
nome = resp = n_barato = ''
while True:
    nome = str(input('Digite o nome do prduto: ')).upper().strip()
    preco = float(input('Digite o valor do produto: R$'))
    total += preco
    cont += 1
    if cont == 1:
        p_barato = preco
        n_barato = nome
    else:
        if preco < p_barato:
            p_barato = preco
            n_barato = nome
    if preco >= 1000:
        totmil += 1
    resp = str(input('Deseja continuar? [S/N] ')).upper().strip()
    if resp in 'S,SIM':
        continue
    else:
        break
print(f'o total de compra foi R${total:.2f}')
print(f'temos {totmil} produtos custando mais de R$ 1000.00')
print(f'o produto mais barato foi {n_barato} que custa R${p_barato}')