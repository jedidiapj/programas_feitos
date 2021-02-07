from datetime import datetime

def voto(n):
    idade = datetime.today().year - n
    print(f'Com {idade} anos:', end=' ')
    if idade <= 18:
        print('Voto negado')
    elif idade >= 18 and idade < 65:
        print('Voto Obrigatório')
    else:
        print('Voto Opcional')
    return idade

n = int(input('Em que ano você nasceu? '))
p1 = voto(n)

