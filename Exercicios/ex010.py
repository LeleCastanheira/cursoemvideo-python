# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
dinheiro = float(input('Quanto dinheiro você tem na carteira? R$ '))
conversor = dinheiro / 3.27
print('Com R${} você pode comprar US${:.2f}'.format(dinheiro, conversor))