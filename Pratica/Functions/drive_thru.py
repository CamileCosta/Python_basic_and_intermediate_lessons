def get_item(x):
  if x == 1:
    return '🍔 Cheeseburger'
  elif x == 2:
    return '🍟 Fries'
  elif x == 3:
    return '🥤 Soda'
  elif x == 4:
    return '🍦 Ice Cream'
  elif x == 5:
    return '🍪 Cookie'
  else:
    return "invalid option"

def welcome():
  print('=========Menu==========')
  print('1 - 🍔 Cheeseburger')
  print('2 - 🍟 Fries')
  print('3 - 🥤 Soda')
  print('4 - 🍦 Ice Cream')
  print('5 - 🍪 Cookie')
  print('=======================')

welcome()

option = int(input('\n What would you like to order? '))
print(get_item(option))