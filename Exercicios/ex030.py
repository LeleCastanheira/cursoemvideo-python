numero = int(input('Diga-me um número qualquer: '))
resto = numero % 2
if resto == 0:
    print('O número {} é PAR'.format(numero))
else:
    print('O número {} é ÍMPAR'.format(numero))
