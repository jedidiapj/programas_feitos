p = int(input('Digite termo: '))
r = int(input('Razão: '))
d = p + (10-1)*r#formula do 10º termo de uma PA
for c in range(p, d, r):
    print('{}'.format(c), end=' -> ')
print("IT'S DONE")