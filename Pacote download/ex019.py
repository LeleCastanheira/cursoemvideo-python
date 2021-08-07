import random
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
lista = (a1, a2, a3, a4)
sorteio = random.choice(lista)
print('O aluno escolhido foi {}'.format(sorteio))

'''
from random import choice
n1 = str(input('Primeiro aluno: ))
n2 = stg(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhino  = choice(lista)
print('O aluno escolhido foi {}'.format(escolhino))
'''