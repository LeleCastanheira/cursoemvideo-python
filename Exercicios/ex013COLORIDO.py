s = float(input('Qual é o salári odo Funcionário? R$ '))
print('O funcionário que ganhava R${}, com {}15% de aumento{}, passa a receber R${:.2f}'.format(s, '\033[1;4m', '\033[m', s+(15/100*s)))
