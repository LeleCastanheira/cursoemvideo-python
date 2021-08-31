from random import randint
from time import sleep
computador = randint(0, 5)
print('\033[1;33m''-=-'*20, '\033[m')
print('\033[1;34m''Vou pensar em um número entre 0 e 5. Tente adivinhar...', '\033[m')
print('\033[1;33m''-=-'*20, '\033[m')
jogador = int(input('\033[1m''Em que número eu pensei? '))
print('\033[35m''PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('\033[31m''PARABÉNS! Você conseguiu me vencer.')
else:
    print('\033[32m''GANHEI! Eu pensei no número {} e não no {}'.format(computador, jogador))
