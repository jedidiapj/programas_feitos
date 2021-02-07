from datetime import date
ano_nascimento = int(input('Digite o seu ano de nascimento: '))
idade = int(date.today().year) - ano_nascimento

if idade <= 9:
    print('Sua idade é {} anos então sua categoria é MIRIM'.format(idade))
elif idade <= 14:
    print('Sua idade é {} anos então sua categoria é INFANTIL'.format(idade))
elif idade <= 19:
    print('Sua idade é {} anos então sua categoria é JUNIOR'.format(idade))
elif idade <= 25:
    print('Sua idade é {} anos então sua categoria é SENIOR'.format(idade))
else:
    print('Sua idade é {} anos então sua categoria é MASTER'.format(idade))

