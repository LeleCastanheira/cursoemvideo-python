n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
n3 = float(input('Terceiro valor: '))
#Verificando o MENOR
menor = n1
if n2 < n1:
    menor = n2
if n3 < n1:
    menor = n3
print('O menor número digitado é {}'.format(menor))
#Verificando o MAIOR
maior = n1
if n2 > n1:
    maior = n2
if n3 > n1:
    maior = n3
print('O maior número digitado é {}'.format(maior))
