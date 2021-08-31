n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
print('Tiranto {} e {}, a média do aluno é {:.1f}'.format(n1, n2, (n1+n2)/2))
if (n1+n2)/2 < 5:
    print('O aluno está {}REPROVADO{}'.format('\033[1;31m', '\033[m'))
elif 5 <= (n1+n2)/2 <= 6.9:
    print('O aluno está em {}RECUPERAÇÃO{}'.format('\033[1;33m', '\033[m'))
elif (n1+n2)/2 >= 7:
    print('O aluno está {}APROVADO{}'.format('\033[1;34m', '\033[m'))
