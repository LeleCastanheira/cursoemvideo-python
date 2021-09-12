# Conversor de temperatura: escreva um programa que converta uma temperatura digitada em ºC para ºF
c = float(input('Informe a temperatura em °C: '))
f = 1.8 * c + 32
print('A temperatura de {}°C corresponde a {}°F!'.format(c, f))