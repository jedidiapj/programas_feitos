aluno = {}
aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Qual a média de {aluno["Nome"]}: '))


if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif aluno['Média'] >= 5:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'

'''print(f'O nome do aluno é {aluno["Nome"]}')
print(f'A média é {aluno["Média"]}')
print(f'Situação = {aluno["Situação"]}')'''

for k, v in aluno.items():
    print(f'O {k} do aluno é {v}')
