dista = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km.'.format(dista))
normal = dista * 0.50
promo = dista * 0.45
if dista <= 200:
    print('E o preço da sua passagem será de {}R${:.2f}{}'.format('\033[1;32m', normal, '\033[m'))
else:
    print('E´o preço da sua pagem será de {}R${:.2f}{}'.format('\033[1;32m', promo, '\033[m'))
