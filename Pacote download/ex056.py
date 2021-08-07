somaidade = 0
media = 0
homem = 0
velho = ''
for p in range(1, 5):
    print('----- {}ª PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        homem = idade
        velho = nome
    if sexo in 'Mm'
media = somaidade /4
print('A média de idade do grupo é de {} anos'.format(media))
