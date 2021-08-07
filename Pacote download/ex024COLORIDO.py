city = str(input('Qual cidade você nasceu? ')).strip()
print('\033[7;32m', city[0:5].lower() == 'santo', '\033[m')
#city começando da letra 0 até o 5
# lower resolve o problema se a pessoa digita em maiúsculo, minúsculo...
