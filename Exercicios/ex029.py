velocidade = int(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    multa = (velocidade  - 80) * 7
    print('MULTADO! Você excedeu o limite permitido que é de 80 Km/h \nVocê dete pagar uma multa de R${}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
