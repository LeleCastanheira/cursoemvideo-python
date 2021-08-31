num = int(input('Digite um número: '))
total = 0                            #números de divisiveis
for c in range(1, num + 1):
    if num % c == 0:                 #se o número for divisível pelo contador
        print('\033[33m', end= '')   #amarelo se for divisível
        total += 1
    else:
        print('\033[31m', end= '')   #vermelho se não for divisível
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezez'.format(num, total))
if total == 2:
    print('E por isso ele é PRIMO')
else:
    print('E por isso ele NAÕ é PRIMO')
