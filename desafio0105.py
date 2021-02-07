def notas(*num, sit=False):
    b = {}
    b['total'] = len(num)
    b['maior'] = max(num)
    b['menor'] = min(num)
    b['média'] = sum(num)/len(num)
    if sit == True:
        if b['média'] < 6:
            b['situação'] = 'Ruim'
            return b
        elif b['média'] >= 6 and b['média'] < 8:
            b['situação'] = 'Boa'
            return b
        elif b['média'] >= 8:
            b['situação'] = 'Otima'
            return b
    return b


#programa principal
resp = notas(8,8,8, sit=True)
print(resp)