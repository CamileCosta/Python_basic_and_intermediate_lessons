from random import randint
computador = randint(0, 5)
print('-' * 20)
print('Vou pensar em um número entre 0 e 5...')
print('-' * 20)
num = int(input('Em q número eu pensei? '))
print('PROCESSANDO...')
if num == computador:
    print('PARABÉNS VC ACERTOU!!')
else:
    print('Que pena, vc errou...')