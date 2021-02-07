def ficha(a='',b=0):
    if a == '':
        a = '<Desconhecido>'
    r = print(f'O jogador {a} fez {b} gols')
    return r


#programa principal
n = str(input('Digite o nome do Jogador: ')).lstrip()
g = input('Digite quantos gols ele fez: ')
if g.isnumeric() == True :
    ficha(n,g)
else:
    g = 0
    ficha(n,g)