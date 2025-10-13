dist = int(input('Insira a distãncia da sua viagem: '))
valor_curto = dist * 0.50
valor_longo = dist * 0.45
if dist <= 200:
    print('Sua viagem vai custar R${}'.format(valor_curto))
else:
    print('Sua viagem vai custar R${} por ser uma distância mais que 200km'.format(valor_longo))