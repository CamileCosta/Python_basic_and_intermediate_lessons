velocidade = int(input('Digite a velocidade do seu carro: '))
multa = velocidade * 7
if velocidade >= 80:
    print('Você foi multado! Com sua velocidade de {}km/h '.format(velocidade))
    print('A sua multa vai custar R${}'.format(multa))
else:
    print('Boa! Você não foi multado!')