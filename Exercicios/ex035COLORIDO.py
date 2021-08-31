print('\033[1;34m''-='*15)
print('Analisador de Triângulos')
print('-='*15, '\033[m')
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r2 < r1 + r3 and r3 < r1 + r2 and r1 < r2 + r3:
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÃO PODEM formar triângulo!')