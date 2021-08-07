p = float(input('Qual é o preço do produto: R$ '))
print('O produto que custava R${}, com {}desconto de 5%{} vai custar R${}{:.2f}{}'.format(p, '\033[4m', '\033[m', '\033[1;32m', p-(5/100 * p), '\033[m'))
