from datetime import date
ano_nascimento = int(input('Digite o seu ano de nascimento: '))
ano_atual = int(date.today().year)
idade = ano_atual - ano_nascimento

if idade < 18:
    ano_alistamento = 18 - idade
    print('Você tem {} anos faltam {} anos para se alistar'.format(idade, ano_alistamento))
    print('Seu alistamento será em {}'.format(ano_atual - ano_alistamento))
elif idade == 18:
    ano_alistamento = 18 - idade
    print('Você tem {} anos está na hora de se alistar'.format(idade))
    print('Seu alistamento será em {}'.format(ano_atual - ano_alistamento))
else:
    ano_alistamento = -(18 - idade)
    print('Você tem {} anos já passou {} anos da hora de se alistar'.format(idade, ano_alistamento))
    print('Seu alistamento foi em {}'.format((ano_atual - ano_alistamento)))
