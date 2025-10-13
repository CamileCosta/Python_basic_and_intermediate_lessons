salario = int(input('Qual o seu salário?'))
aumento_sup = salario + (salario * 10/100)
aumento_inf = salario + (salario * 15/100)
if salario >= 1250.00:
    print('Seu aumento será de R${} por ser maior que R$1250.00'.format(aumento_sup))
else:
    print('Seu aumento será de R${} por ser menor que R$1250,00'.format(aumento_inf))
