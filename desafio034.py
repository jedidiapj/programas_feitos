salario_fun = float(input('Digite o seu salário:\n'))

if salario_fun >= 1250.00:
    aumento1 = salario_fun + (salario_fun*(10/100))
    print('Seu novo salario é: R${:.2f}'.format(aumento1))
else:
    aumento2 = salario_fun + (salario_fun*(15/100))
    print('Seu nome salario é: R${:.2f}'.format(aumento2))
