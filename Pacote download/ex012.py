p = float(input('Digite o preço do produto: R$ '))
m = p * 0.05
des = p - m
print('O preço que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(p, des))
