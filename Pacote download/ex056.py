somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher = 0
for p in range(1, 5):      #p = pessoa
    print('----- {}ª PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher += 1
media = somaidade /4
print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} ano e seu nome é {}.'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulher(es) com menos de 20 anos.'.format(totmulher))
