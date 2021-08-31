from time import sleep
n = input('Digite seu nome completo: ')
print('Analisando seu nome...')
sleep(2)
print('Seu nome em maiúscula é {}{}{}'.format('\033[1;34m', n.upper(), '\033[m'))
print('Seu nome em minúscula é {}{}{}'.format('\033[1;31m', n.lower(), '\033[m'))
print('Seu nome tem ao todo {}{}{} letras'.format('\033[1;34m', len(n)-n.count(' '), '\033[m'))
d = n.split()
print('Seu primeiro nome é {}{} e ele tem {}{} letras'. format('\033[1;4;31m', d[0], len(d[0]), '\033[m'))
