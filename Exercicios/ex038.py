n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('O {}PRIMEIRO{} valor é maior'.format('\033[1;4m', '\033[m'))
elif n1 < n2:
    print('O {}SEGUNDO{} valor é maior'.format('\033[1;4m', '\033[m'))
elif n1 == n2:     #tbm poderia ser else, pois se não é > ou < é =
    print('Os dois números são {}iguais'.format('\033[1;4m'))
