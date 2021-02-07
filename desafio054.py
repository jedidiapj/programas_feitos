from datetime import datetime
ano_atual= datetime.today().year
cont = 0
cont2 = 0
for c in range(1,8):
    ano = int(input('Diga seu ano de nascimento: '))
    idade = ano_atual - ano
    if idade >= 18:
        cont += 1
    else:
        cont2 += 1
print('{} pessoas são maior de idade e {} são menores de idade'.format(cont, cont2))
