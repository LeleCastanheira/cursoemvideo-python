d = float(input('Quanto dinheiro você tem na caeteira: R$ '))
print('Com R${} você pode comprar\n{}U$ {:.2f}{}'.format(d, '\033[1;32m', d/5.27, '\033[m'))
print('{}€ {:.2f}{}'.format('\033[1;36m', d/6.39, '\033[m'))
print('{}¥ {:.2f}{}'.format('\033[1;31m', d*20.77, '\033[m'))
