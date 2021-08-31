n = int(input('\033[1;35m''Me diga um número qualquer: ''\033[m'))
resto = n % 2
if resto == 0:
    print('O número {} é {}PAR{}'.format(n, '\033[1;34m', '\033[m'))
else:
    print('O número {} é {}ÍMPAR{}'.format(n, '\033[1;34m', '\033[m'))
