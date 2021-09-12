'''Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens de até 200km
e R$ 0,45 para viagens mais longas'''
km = int(input('Qual é a distância de sua viagem? '))
normal = 0.50 * km
promo = 0.45 * km
print('Você está prestes a começar uma viagem de {}Km'.format(km))
if km <= 200:
    print('E o preço da sua passagem será de R${:.2f}'.format(normal))
else:
    print('E o preço da sua passagem será de R${:.2f}'.format(promo))

'''Condição Simplificada
km = float(iput('Qual é a distância da sua viagem? '))
print('Você está preste a começar uma viagem de {}Km'.format(km))
preço = km * 0,50 if km <= 200 else km 0,45
print(E o preço da sua passagem será de R${:.2f}'.format(preço))'''