n = int(input('Digite um número: '))
print('O dobro de {} vale {}{}{}'.format(n, '\033[7;46m', n * 2, '\033[m'))
print('O tripo de {} vale {}{}{}'.format(n, '\033[7;46m', n * 3, '\033[m'))
print('A raiz quadrada de {} é igual a {}{:.2f}{}'.format(n, '\033[7;46m', n ** (1/2), '\033[m'))