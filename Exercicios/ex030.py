'''Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.'''
numero = int(input('Diga-me um número qualquer: '))
resto = numero % 2
if resto == 0:
    print('O número {} é PAR'.format(numero))
else:
    print('O número {} é ÍMPAR'.format(numero))
