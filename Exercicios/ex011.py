# Faça um programa que leia a largura e a algura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²
l = float(input('Largura da parede: '))
h = float(input('Altura da parede: '))
a = l * h
q = a / 2
print('Sua parede tem a dimensão, em metros, de {} x {} e sua área é de {}m².\nPara pinta essa parede, você precisará de {}L de tinta.'.format(l, h, a, q))