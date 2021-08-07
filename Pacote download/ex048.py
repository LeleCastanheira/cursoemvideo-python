soma = 0     #acumuladores (aprenderá na aula 14)
cont = 0     #contador (aprenderá na aula 14)
for c in range(1,501, 2):  #números ímpares
    if c % 3 == 0:         #divisível por 3
        cont += 1       #cont = cont + 1  #O contador geralmente conta +1
        soma += c       #soma = soma + c  #O acumulador soma/multiplica... valores
print('A soma de todos os {} valores solicitados é {}'. format(cont, soma))
