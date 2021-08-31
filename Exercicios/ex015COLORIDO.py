d = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
print('O total a pagar é de ''\033[;33m''R${:.2f}''\033[m'.format(60*d + 0.15*km))
