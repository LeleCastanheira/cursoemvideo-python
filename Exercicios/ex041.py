from datetime import date
nasc = int(input('Ano de Nascimento: '))
idade = date.today().year - nasc
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('Classificação: {}MIRIM{}'.format('\033[1;7;97;40m', '\033[m'))
elif idade <= 14:
    print('Classificação: {}INFANTIL{}'.format('\033[1;7;34m;107', '\033[m'))
elif idade <= 19:
    print('Classificaçao: {}JÚNIOR{}'.format('\033[1;7;33;107m', '\033[m'))
elif idade <= 25:
    print('Classificação: {}SÊNIOR{}'.format('\033[1;7;32;107m', '\033[m'))
else:
    print('Classificação: {}MASTER{}'. format('\033[1;7;30;107m', '\033[m'))
