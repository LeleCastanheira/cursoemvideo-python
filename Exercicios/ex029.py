'''Escreva um programa que leia a velocidade de um carro
Se ele ultrapassar 80km / h, mostre uma mensagem dizendo que ele foi multado
A multa vai custar R $ 7,00 por cada Km acima do limite.'''
velocidade = int(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    multa = (velocidade  - 80) * 7
    print('MULTADO! Você excedeu o limite permitido que é de 80 Km/h \nVocê dete pagar uma multa de R${}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
