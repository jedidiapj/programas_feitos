from time import sleep
valor_casa = float(input('Digite o valor da casa:\nR$'))
salario = float(input('Digite seu salário:\nR$'))
tempo_pagamento = int(input('Em quantos anos pretende pagar?\n'))

cond_salario = salario*30/100
valor_mensal = valor_casa/(tempo_pagamento*12)

print('Estamos analisando sua solicitação só um momento')
sleep(1)
print('.')
sleep(1)
print('.')
sleep(1)
print('.')
sleep(1)
if cond_salario >= valor_mensal:
    print('''Seu \33[1;33mempréstimo foi autorizado\33[m.
iremos providenciar o contrato.''')
else:
    print('\33[1;31mEmprestimo não aprovado\33[m')
