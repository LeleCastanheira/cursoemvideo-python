num = int(input('Digite um número inteiro: '))
print('''Escolha uma das basaes para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
op = int(input('Sua opção: '))
if op == 1:
    print('{} convertido para ''\033[1;33m''BINÁRIO ''\033[m''é igual a {}'.format(num, bin(num)[2:]))
elif op == 2:
    print('{} convertido para {}OCTAL{} é igual a {}'.format(num, '\033[1;34m', '\033[m', oct(num)[2:]))
elif op == 3:
    print('{} convertido para {}HEXADECIMAL{} é igual a {}'. format(num, '\033[1;35m', '\033[m', hex(num)[2:]))
else:
    print('\033[1;31m''Opção inválida. Tente novamente.''\033[m')
