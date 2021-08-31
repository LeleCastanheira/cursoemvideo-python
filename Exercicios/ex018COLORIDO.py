from math import radians, sin, cos, tan
n = float(input('digite o ângulo que você deseja: '))
s = sin(radians(n))
c = cos(radians(n))
t = tan(radians(n))
print('{}O ângulo de {} tem o seno de {:.2f}'.format('\033[4m', n, s))
print('O ângulo de {} tem o cosseno de {:.2f}'.format(n, c))
print('O ângulo de {} tem a tangente de {:.2f}{}'.format(n, t, '\033[m'))
