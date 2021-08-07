salario = float(input('Qual é o seu salário do funcionário? R$ '))
if salario > 1250:
    aumento = (salario * 10/100) + salario
else:
    aumento = (salario * 15/100) + salario
print('Quem ganhava R$ {} passa a ganhar R$ {} agora.'.format(salario, aumento))
