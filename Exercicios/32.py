ano = int(input('Digite um ano: '))
if ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0:
    print('O ano {} é bissexto!'.format(ano))
else:
    print('O ano digitado não é bissexto!')