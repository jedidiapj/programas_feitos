valores = []
for p in range(0,5):
    n = int(input(f'Digite o {p+1}º número: '))
    if p == 0 or n > valores[-1]: # se n for maior q o ultimo elemento da lista
        valores.append(n)
        print('Valor adicionado ao fim da lista')
    else: # para saber em que posição se deve colocar o menor valor
        pos = 0
        while pos < len(valores): # busca da posição 0 até o fim da lista
            if n <= valores[pos]: # verifica se o valor que ocupa 0 eh maior que n
                valores.insert(pos,n) # se for maior insere o menor valor
                print(f'Valor adicionado na posição {pos} da lista')
                break
            pos += 1
print(valores)
