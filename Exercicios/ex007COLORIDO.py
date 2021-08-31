n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segundo nota do aluno: '))
print('A média entre {} e {} é igual a {}{}{}'.format(n1, n2, '\033[4;35;107m', (n1 + n2) / 2, '\033[m'))
