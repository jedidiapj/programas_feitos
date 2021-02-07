from datetime import datetime

cadastro = dict()
cadastro['Nome'] = str(input('Digite seu nome: '))
ano_nasc = int(input('Ano de nascimento: '))
cadastro['Idade'] = datetime.today().year - ano_nasc
cadastro['CTPS'] = int(input('Digite o numero da CTPS: [0 se não tiver]'))

if cadastro['CTPS'] != 0:
    cadastro['Ano de contratação'] = int(input('Ano de contratação: '))
    aposentadoria = cadastro['Idade'] + (35 - (datetime.today().year - cadastro['Ano de contratação']))
    cadastro['Salário'] = float(input('Qual seu salário? '))
    cadastro['Aposentadoria'] = aposentadoria
print('-='*20)

for k, v in cadastro.items():
    print(f'{k} tem o valor {v}')
