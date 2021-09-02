'''from math import factorial
n = int(input('Digite um número para calcular seu fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}'.format(n, f))'''

       #USANDO WHILE
'''n = int(input('Digite um número para calcular seu fatorial: '))
contador = n     #o contador começa com o número que acabou de ler
f = 1
print('Calculando {}! = '.format(n), end='')
while contador > 0:
    print('{}'.format(contador), end='')
    print(' x ' if contador > 1 else ' = ', end='')
    f *= contador
    contador -= 1
print(f)'''

        #USANDO FOR
n = int(input('Digite um número para calcular seu fatorial: '))
contador = n
f = 1
print('Calculando {}! = '.format(n), end='')
for contador in range(n,0,-1):
    print('{}'.format(contador), end='')
    if contador > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')    
    f *= contador
    contador -=1
print(f)