maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('O peso da {}ª pessoa: '.format(p)))
    if p == 1:             #o peso da 1ª pessoa
        maior = peso       #o maior peso será o peso
        menor = peso       #o menor peso será o peso
    else:
        if peso > maior:   #se o peso que acabei de ler for maior do que o maior peso que tenho
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}Kg'.format(maior))
print('O menor peso lido foi de {}Kg'.format(menor))
