# Aluguel de carros:
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado
# Calcule o preço a pagar, sabendo que o carro custa R $ 60 por dia e R $ 0,15 por km rodado
d = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodaddos? '))
dias = d * 60
rodados = 0.15 * km
total = dias + rodados
print('O total a pagar é de R${:.2f}'.format(total))