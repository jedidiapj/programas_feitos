nome = input('Digite seu Nome:\n')
salario = float(input('Digite seu salário:\n'))

nS = salario+salario*(15/100)

print('Parabéns {} seu novo sálario é R${:.2f}'.format(nome, nS))
