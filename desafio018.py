from math import sin, cos, tan, radians
a1 = float(input('Digite o angulo que você deseja: '))
s1 = sin(radians(a1))
c1 = cos(radians(a1))
t1 = tan(radians(a1))

print('O Seno de {} é: {:.2f}\n\nO Cosseno de {} é: {:.2f}\n\nA tangente de {} é: {:.2f}'.format(a1, s1, a1, c1, a1, t1))
