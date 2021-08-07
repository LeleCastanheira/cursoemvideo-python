print('{:=^20}'.format(' STORE '))
preco = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/pix
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    desconto = preco - (10/100 * preco)
    print('Sua compra de R$ {:.2f} vai custar R$ {:.2f}'.format(preco, desconto))
elif opcao == 2:
    desconto = preco - (5/100 * preco)
    print('Sua compra de R$ {:.2f} vai custar R$ {:.2f}'.format(preco, desconto))
elif opcao == 3:
    print('Sua compra será parcelada em 2x de R$ {:.2f} sem juros'.format(preco/2))
elif opcao == 4:
    juros = preco + (20/100 * preco)
    parcelas = int(input('Quantas parcelas? '))
    total = juros/parcelas
    print('Sua compra será parcelada em {}x de R$ {:.2f} com juros'.format(parcelas, total))
    print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(preco, juros))
else:
    print('{}OPÇÃO INVÁLIDA{}'.format('\033[1;31m', '\033[m'))
