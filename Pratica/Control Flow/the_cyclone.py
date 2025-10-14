print('Lets see if you can ride!')

height = int(input('How many heights do you have(cm)? '))

credits = int(input('How many credits do you have? '))

if height >= 137 and credits >= 10:
  print('Enjoy the ride!')
elif height < 137 and credits >= 10:
  print('You are not tall enough to ride.')
elif height >= 137 and credits < 10:
  print('You dont have enough credits.')
else:
  print('You dont have both requirement')