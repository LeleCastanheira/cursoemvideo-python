d = float(input('Digite uma diatância em metros: '))
print('A medida de {}m corresponde a'.format(d))
print('\033[1;33;107m''{}km\n{}hm\n{}dm\n{}dm\n{}cm\n{}mm'.format(d/1000, d/100, d/10, d*10, d*100, d*1000))
