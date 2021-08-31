l = float(input('Largura da parede: '))
h = float(input('Altura da parede: '))
print('Sua parede tem a dimensão de {} x {} e área de {}{}{}m².'.format(l, h, '\033[1;4m', l*h, '\033[m'))
print('Para pintar essa parede, você precisará de {}{:.2f}{}L de tinta.'.format('\033[1;4;34m', (l*h)/2, '\033[m'))
