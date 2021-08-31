peso = float(input('Qual é seu peso? (kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está {}ABAIXO{} do peso normal'.format('\033[1;31m', '\033[m'))
elif 18.5 <= imc < 25:
    print('Você está no {}PESO IDEAL{}'.format('\033[1;32m', '\033[m'))
elif 25 <= imc < 30:
    print('Você está com {}SOBREPESO{}'.format('\033[1;33m', '\033[m'))
elif 30 <= imc < 40:
    print('Você está com {}OBESIDADE{}'.format('\033[1;35m', '\033[m'))
else:
    print('Você está com {}OBESIDADE MÓRBIDA{}'.format('\033[1;30m', '\033[m'))
