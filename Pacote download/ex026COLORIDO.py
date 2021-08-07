frase = str(input('Digite uma frase: ')).strip().lower()
print('\033[1;33m''A letra A aparece {} vezes na frase.''\033[m'.format(frase.count('a')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('a')+1))
print('\033[1;33m''A última letra A aoareceu na posição {}''\033[m'.format(frase.rfind('a')+1))
