primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão: '))
acumulador = 1
total = 0
mais = 10   #O exercício já pede os 10 primeiros termos
while mais != 0:
    total = total + mais
    while acumulador <= total:
        print(primeiro_termo, end=' ➤  ')
        primeiro_termo += razao
        acumulador += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))