valores = []
while True:
    n = int(input('Digite um número: '))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso')
    else:
        print('valor duplicado por gentileza utilizar outro.')
    opcao = str(input('Deseja coninuar? [S/N] ')).upper().strip()
    if opcao in 'N,NÃO':
        break
print(sorted(valores))

