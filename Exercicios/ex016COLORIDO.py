from math import trunc
n = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua {}porção inteira é {}{}'.format(n, '\033[1;4;7m', trunc(n), '\033[m'))
