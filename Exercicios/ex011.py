l = float(input('Largura da parede: '))
h = float(input('Altura da parede: '))
a = l * h
q = a / 2
print('Sua parede tem a dimensão, em metros, de {} x {} e sua área é de {}m².\nPara pinta essa parede, você precisará de {}L de tinta.'.format(l, h, a, q))
