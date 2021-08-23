from time import sleep
n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    opcao = int(input('>>>>> Qual é sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma é {}'.format(soma))
        sleep(0.5)
    elif opcao == 2:
        produto = n1 * n2
        print('A multiplicação é {}'.format(produto))
        sleep(0.5)
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior é {}'.format(maior))
        sleep(0.5)
    elif opcao == 4:
        print('Informe os número novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
        sleep(0.5)
    elif opcao == 5:
        print('Finalizando...')
        sleep(0.5)
    else:
        print('Opção inválida. Tente novamete')
        sleep(0.5)
print('Fim do programa. Volte sempre!')