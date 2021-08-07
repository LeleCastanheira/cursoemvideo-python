'''from math import pow, sqrt
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimeto do cateto adjacente: '))
sq = pow(co, 2) + pow(ca, 2)
hip = sqrt(sq)
print('A hipotenusa medirá {:.2f}'.format(hip))

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hip = (ca**2 + co**2) * (1/2)
print('A hipotenusa é {:.2f}'.format(hip))'''

from math import hypot
co = float(input('Comprimeto do cateto oposto: '))
ca = float(input('Comprimeto do cateto adjacente: '))
print('A hipotenusa vale {:.2f}'.format(hypot(ca, co)))
