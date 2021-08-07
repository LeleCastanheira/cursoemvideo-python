frase = str(input('Digite uma frase: ')).strip().upper()
#dividir as palavras da frase em uma lista
palavras = frase.split()
#juntar todas as palvras sem espaço da lista
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1): #vai pegar a última letra, vai até -1(antes da primeira), e volta uma letra
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')