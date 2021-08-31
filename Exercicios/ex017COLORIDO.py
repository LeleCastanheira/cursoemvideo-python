from math import hypot
co = float(input('Comprimeto do cateto oposto: '))
ca = float(input('Comprimeto do cateto adjacente: '))
print('{}A hipotenusa vale {:.2f}{}'.format('\033[7m', hypot(ca, co), '\033[m'))
