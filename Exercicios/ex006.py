# Crie um algoritmo que leia um número e mostre o seu dobro, o seu triplo e sua raiz quadrada:
n1 = int(input('Digite um número: '))
d = n1 * 2
t = n1 * 3
r = n1 ** (1/2)
print('O dobro de {} vale {}.\nO triplo de {} vale {}.\nA raiz quadrada de {} é igual a {:.2f}.'.format(n1, d, n1, t, n1, r))