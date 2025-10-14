guess = 0
tries = 0 #para adiocionar quantas tentativas possiveis ate adivinhar certo

while guess != 6 and tries < 5:
  guess = int(input('Guess the number: '))
  tries += 1

if tries == 5:
  print('No more chances!')

if guess == 6:
  print('You got it!')