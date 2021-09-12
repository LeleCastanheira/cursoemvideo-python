# Escreva um programa que leia um valor em metros e o exiba convertido em taxa e quilômetro
m = float(input('Uma distância em mentro: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print('A medida de {} m corresponde a:\n{}km\n{}hm\n{}dam\n{:.0f}dm\n{:.0f}cm\n{:.0f}mm'.format(m, km, hm, dam, dm, cm, mm))