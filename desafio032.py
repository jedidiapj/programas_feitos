from datetime import date
ano = int(input('Digite um ano\nPara analisar o ano atual digite 0\n'))
ano_bisexto = ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0

if ano == 0:
    ano = date.today().year
if ano_bisexto == 0:
    print('{} é um ano Bissexto'.format(ano))
else:
    print('{} não é um ano Bissexto'.format(ano))
