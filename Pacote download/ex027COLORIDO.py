nome = str(input('Digite seu nome completo: ')).strip()
print('\033[1;7;35m','Muito prazer te conhecer!{}'.format('\033[m'))
d = nome.split()
print('Seu primeiro nome é {}'.format(d[0]))
print('Seu último nome é {}'.format(d[-1]))
