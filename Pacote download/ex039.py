from datetime import date
print('''Escolha o seu sexo:
[ 1 ] Feminino
[ 2 ] Masculino''')
op = int(input('Sua opção: '))
if op == 2:
    nasc = int(input('Ano de nascimento: '))
    idade = date.today().year - nasc
    print('Quem nasceu em {} tem/fará {} anos em {}'.format(nasc, idade, date.today().year))
    if idade < 18:
        print('Ainda faltam {}{}{} ano(s) para o alistamento.'.format('\033[1;32m', 18 - idade, '\033[m'))
        print('Seu alistamento será em {}{}{}'.format('\033[1;4m', date.today().year + 18 - idade, '\033[m'))
    elif idade == 18:
        print('Você tem que se alistar {}IMEDIATAMENTE{}'.format('\033[1;4m', '\033[m'))
    elif idade > 18:
        print('Você deveria ter se alistado há {}{} ano(s){}'.format('\033[1;4m', idade - 18, '\033[m'))
        print('Seu alistamento foi em {}'.format(date.today().year - (idade - 18)))
elif op == 1:
    print('Muito obrigado!')
else:
    print('\033[1;31m''Opção inválida. Tente novamente.''\033[m')
