casa = float(input('Valor da casa: R$ '))
sal = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prest = casa / (anos * 12)
min = sal * 30/100
print('Para pagar uma casa de R${} em {} ano(s), a prestação será de R$ {:.2f}'.format(casa, anos, prest))
if prest <= min:
    print('Empréstimo pode ser {}CONCEDIDO!{}'.format('\033[1;32m', '\033[m'))
else:
    print('Empréstimo {}NEGADO!{}'.format('\033[1;31m', '\033[m'))
