weight = float(input('What is your Earth weight? '))

planet = int(input('Enter a planet number: '))

if planet == 1:
  destination = weight * 0.38
  print('You chose Mercury and your weight on the destination is {:.2f}'.format(destination))
elif planet == 2:
  destination = weight * 0.91
  print('You chose Venus and your weight on the destination is {:.2f}'.format(destination))
elif planet == 3:
  destination = weight * 0.38
  print('You chose Mars and your weight on the destination is {:.2f}'.format(destination))
elif planet == 4:
  destination = weight * 2.53
  print('You chose Jupiter and your weight on the destination is {:.2f}'.format(destination))
elif planet == 5:
  destination = weight * 1.07
  print('You chose Saturn and your weight on the destination is {:.2f}'.format(destination))
elif planet == 6:
  destination = weight * 0.89
  print('You chose Uranus and your weight on the destination is {:.2f}'.format(destination))
elif planet == 7:
  destination = weight * 1.14
  print('You chose Neptune and your weight on the destination is {:.2f}'.format(destination))
else:
  print('Invalid planet number')