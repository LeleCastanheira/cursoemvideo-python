d = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodaddos? '))
dias = d * 60
rodados = 0.15 * km
total = dias + rodados
print('O total a pagar é de R${:.2f}'.format(total))
