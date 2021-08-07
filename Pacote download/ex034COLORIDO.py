sal = float(input('\033[1m''Qual é o salário do funcionário? R$''\033[m'))
if sal > 1250:
    aumento = (sal * 10/100) + sal
else:
    aumento = (sal * 15/100) + sal
print('\033[1;32m''Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(sal, aumento))
