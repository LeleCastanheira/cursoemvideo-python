# Desafio 16: Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua totalidade.

'''from math import trunc
n = float(input('Digite um número: '))
print('O número {} tem a parte Inteira {}'.format(n, trunc(real)))'''

n = float(input('Digite um número: '))
print('O número {} tem a parte inteira {}'.format(n, int(n)))