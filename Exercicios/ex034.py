'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento
Para salários superiores a R$ 1.250,00, calcule um aumento de 10%
Para os inferiores ou iguais, o aumento é de R$ 15%.'''
salario = float(input('Qual é o seu salário do funcionário? R$ '))
if salario > 1250:
    aumento = (salario * 10/100) + salario
else:
    aumento = (salario * 15/100) + salario
print('Quem ganhava R$ {} passa a ganhar R$ {} agora.'.format(salario, aumento))
