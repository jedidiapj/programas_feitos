idade = cont = soma = homens = mulheres = m_menor = 0
sexo = op = ''
while True:
    idade = int(input('Digite uma idade: '))
    sexo = str(input('Qual o sexo: [M/F] ')).upper().strip()
    op = str(input('Quer continuar a digitar? ')).upper().strip()
    if idade >= 18:
        cont += 1
    elif sexo in 'M':
        homens += 1
    elif sexo == 'F':
        mulheres += 1
        if idade < 20:
            m_menor += 1
    if op in 'S,SIM':
        continue
    else:
        break
print(f'existem {cont} homens acima de 18 anos')
print(f'foram {homens} homens cadastrados')
print(f'foram cadastradas {mulheres} mulheres e entre elas {m_menor} são menores de idade')
