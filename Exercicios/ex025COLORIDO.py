nome = str(input('Qual é seu nome completo? ')).strip()
print('Seu nome tem Silva? ''\033[4;7m''{}''\033[m'.format('silva' in nome.lower()))