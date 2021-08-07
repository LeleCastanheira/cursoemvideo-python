velocidade = int(input('Qual é a velocidade do carro? '))
multa = (velocidade - 80)*7
if velocidade > 80:
    print('\033[1;31m''MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    print('Você deve pagar uma multa de {}R${:.2f}{}'.format('\033[1;33m', multa, '\033[m'))
print('\033[1;32m''Tenha um bom dia! Dirija com segurança!''\033[m')
