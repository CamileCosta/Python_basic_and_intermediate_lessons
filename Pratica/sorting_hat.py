print('Lets decide which House of Harry Potter is yours!')

Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

print('Q1) Do you like Dawn or Dusk? ')
print('1) Dawn')
print('2) Dusk')
Q1 = int(input('Your answer: '))

if Q1 == 1:
  Gryffindor += 1
  Ravenclaw += 1
elif Q1 == 2:
  Hufflepuff += 1
  Slytherin += 1
else:
  print('Wrong input')

print("Q2) When I'm dead, I want people to remember me as: ")
print('1) The Good')
print('2) The Great')
print('3) The Wise')
print('4) The Bold')
Q2 = int(input('Your answer: '))

if Q2 == 1:
  Hufflepuff += 2
elif Q2 == 2:
  Slytherin += 2
elif Q2 == 3:
  Ravenclaw += 2
elif Q2 == 4:
  Gryffindor += 2
else:
  print('Wrong input')

print('Q3) Which kind of instrument most pleases your ear? ')
print('1) The violin')
print('2) The trumpet')
print('3) The piano')
print('4) The drum')
Q3 = int(input('Your answer: '))

if Q3 == 1:
  Slytherin += 4
elif Q3 == 2:
  Hufflepuff += 4
elif Q3 == 3:
  Ravenclaw += 4
elif Q3 == 4:
  Gryffindor += 4
else:
  print('Wrong input')

print('Gryffindor = {}'.format(Gryffindor))
print('Ravenclaw = {}'.format(Ravenclaw))
print('Hufflepuff = {}'.format(Hufflepuff))
print('Slytherin = {}'.format(Slytherin))