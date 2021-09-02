primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão: '))
acumulador = 1
while acumulador <= 10:
    print(primeiro_termo, end=' ➤  ')
    primeiro_termo += razao
    acumulador += 1
print('FIM')